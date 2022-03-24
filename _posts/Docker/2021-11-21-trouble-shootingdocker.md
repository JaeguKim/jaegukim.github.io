---
layout: post
title: "Trouble Shooting(Docker)"
date: 2021-11-21 16:29:00 +0900
categories: [Docker]
---

## COPY 커멘드시 wildcard 사용
`COPY src/* dest/` : src내에 있는 subdirectory 구조를 고려하지 않고, 파일들을 dest 경로로 복사
`COPY src/ dest/` : subdirectory 구조를 고려하여 복사

## deadsnakes repository에서 Python 설치시 버전 못찾는 이슈 해결

python 3.7뒤에 `3.7.13-1+focal1` 이런식으로 정확한 버전을 명시해두면, 최신 버전이 출시될시 해당 버전이 삭제되면 설치가 안된다.
따라서 아래처럼 와일드카드 형식으로 명시해두어 최신버전을 받아오도록 해결.
사실 버전을 명시해두지 않으면 자동으로 최신버전으로 설치하는 것같지만 hadolint에서 에러를 뱉으므로 이렇게 하는게 좋은듯함.
```Dockerfile
RUN apt-get update -y \
    && apt-get install software-properties-common=0.98.9.5 -y \
    && add-apt-repository ppa:deadsnakes/ppa \
    && apt-get install -y --no-install-recommends \
    python3.7=* \
    python3.7-dev=* \ 
```

