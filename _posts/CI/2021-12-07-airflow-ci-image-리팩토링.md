---
layout: post
title: "Airflow ci image 리팩토링"
date: 2021-12-07 16:11:00 +0900
categories: [CI]
---

## Airflow ci image 리팩토링 계기
airflow 컨테이너에 `requirements.txt`에 정의된 패키지들을 설치할때, 기존에는 legacy resolver를 사용하여 설치를 했었다.(`pip3 install --no-cache-dir --use-deprecated=legacy-resolver -r /etc/requirements.txt`) 이 legacy resolver는 패키지 버전 충돌을 고려하지 않기때문에 airflow 스크립트가 실행도중 정확한 패키지 버전의 모듈을 참조하지 못해 에러가 발생할 수 있다. legacy resolver를 걷어냈더니 이제는 모듈 버전 conflict가 발생하였다. 이 과정에서 conflict이 발생하지 않도록 버전을 찾는과정은 굉장히 시간소모적인 일이므로 편리한 dependency resolving 기능을 제공하는 Poetry를 도입하기로 했다.

## Poetry POC
- Poetry의 장점 : 편리한 dependency resolving, 가상환경 구성, whl packaging
- Package 설치방식
    1. poetry update : toml 파일에 있는 package들을 dependency resolving 하여 poetry.lock 파일생성
    2. poetry install : poetry.lock 에 있는 package 설치
- 문제점 : Package 설치 및 resolving 시간이 오래걸림

## 도입시 문제점
### 도커빌드시간 증가
Poetry를 도입한 버전으로 airflow ci image를 리팩토링 했을때, 빌드시 14분소요 (pip으로 설치시 5분~6분 소요) 되었다.
병목은 `poetry update` 이다. `poetry update` 가 실행되면 `pyproject.toml` 파일에 정확한 패키지 버전을 명시해주었다고 하더라도, 모든 패키지들간의 상호 의존성을 고려해서 버전을 탐색하게 된다.
이를 최적화하기 위해서 `poetry update`를 로컬에서 수행후 `poetry.lock` 파일을 함께 커밋하고 `poetry install` 만 수행하여 빌드를 최적화할수는 있다. 하지만 그렇게 해도 여전히 빌드 시간이 오래걸린다.

```Dockerfile
FROM summerwind/actions-runner:v2.283.1-ubuntu-20.04

ENV PYTHONPATH="/usr/local/airflow/dags:${PYTHONPATH}"

USER root

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

RUN apt-get update -y \
    && apt install software-properties-common -y \
    && add-apt-repository ppa:deadsnakes/ppa \
    && apt-get install -y \
    apt-transport-https \
    gcc \
    gpg-agent \
    librdkafka-dev \
    make \
    vim \
    default-libmysqlclient-dev \
    libssl-dev \
    build-essential=* \
    python3.7 \
    python3.7-dev \
    && ln -sf /usr/bin/python3.7 /usr/bin/python3 \
    && ln -sf /usr/bin/python3.7 /usr/bin/python \
    && rm -rf /var/lib/apt/lists/*

USER runner

COPY pyproject.toml poetry.lock /
ENV PATH /root/.local/bin:$PATH
RUN pip install --upgrade pip \
    && pip install --no-cache-dir poetry==1.1.11 \
    && poetry config virtualenvs.create false \
    && poetry install \
    && airflow db init

ENTRYPOINT ["/usr/local/bin/dumb-init", "--"]
CMD ["/entrypoint.sh"]
```

## 해결과정
Poetry는 airflow처럼 도커이미지가 자주 빌드되어야 하고, 설치해야하는 dependency가 많은 경우에는 적합하지 않은것으로 보인다. 따라서 `requirements.txt`를 사용하기로 했고 [airflow 공식레포의 패키지 버전 명세](https://github.com/apache/airflow/blob/constraints-2.1.3/constraints-3.7.txt)를 참고해서 패키지 버전을 세팅해주었다. 이때 명세에 존재하지 않는 패키지들도 존재하는데 이때는 버전을 알아내고 싶은 패키지 버전의 정보를 빈 상태로 두었다. 그리고 가상 환경에 `pip3 install requirements.txt`를 수행한다음 `pip3 list` 커멘드를 실행해 해당 패키지 버전을 찾아주었다.

``` Dockerfile
FROM summerwind/actions-runner:v2.283.1-ubuntu-20.04

LABEL maintainer="jaegoo.kim@pubg.com"

ENV PYTHONPATH="/usr/local/airflow/dags:${PYTHONPATH}"

USER root

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

RUN apt-get update -y \
    && apt-get install software-properties-common=0.98.9.5 -y \
    && add-apt-repository ppa:deadsnakes/ppa \
    && apt-get install -y --no-install-recommends \
    default-libmysqlclient-dev=1.0.5ubuntu2 \
    libssl-dev=1.1.1f-1ubuntu2.8 \
    build-essential=12.8ubuntu1.1 \
    python3.7=3.7.12-1+focal1 \
    python3.7-dev=3.7.12-1+focal1 \
    && ln -sf /usr/bin/python3.7 /usr/bin/python3 \
    && ln -sf /usr/bin/python3.7 /usr/bin/python \
    && rm -rf /var/lib/apt/lists/*

USER runner

COPY requirements.txt requirements-ci.txt /
ENV AIRFLOW__CORE__DAGS_FOLDER /runner/_work/airflow/airflow/dags/
RUN pip install --no-cache-dir --upgrade pip==21.3 \
    && pip install --no-cache-dir -r requirements.txt \
    && pip install --no-cache-dir -r requirements-ci.txt \
    && airflow db init
ENTRYPOINT ["/usr/local/bin/dumb-init", "--"]
CMD ["/entrypoint.sh"]
```