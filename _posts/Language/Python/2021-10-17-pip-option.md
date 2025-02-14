---
layout: post
title: "pip option"
date: 2021-10-17 12:04:00 +0900
categories: [Language,Python]
---

## --no-cache-dir
disable cache
여기서 말하는 cache란 아래와 같다. 
- pip으로 설치하는 모듈들의 설치파일들(.whl 등)
- source file(.tar.gz등)들
사용하는 이유는 도커 이미지를 가능하면 작게 유지하기 위해서이거나 공간을 절약하기 위해서이다.


## -e option

pip install을 할때 -e를 flag로 주면 설치한 패키지의 소스코드의 수정이 ```pip install``` 한번더 할 필요없이 바로 환경에 반영이 된다. 주로 로컬에서 패키지를 테스트하는 용도로 사용이된다고 한다.

다음 [링크](https://stackoverflow.com/a/35064498)를 살펴보면 좋다.

## --user option

보통 시스템 Python에 모듈을 설치하는 경우 권한 문제가 발생한다. 이를 해결하기 위해서 sudo 커멘드를 쓸수도 있지만 시스템 파이썬에 모듈을 설치하는것은 좋은 방법이 아니다.
따라서 보통 virtualenv를 사용하거나 --user를 사용한다. --user 옵션을 사용하면 시스템 디렉토리가 아닌 유저 현재 유저 디렉토리에 모듈이 설치가 되어서, 시스템을 망가뜨릴 위험이 없다.

단, 해당 모듈을 커멘드라인에서 사용하려면 .zshrc 파일에 다음 라인을 추가해야한다.

``` sh
export PATH=$PATH:/Users/[username]/Library/Python/[python version]/bin
```

## install optional sub-packages

다음처럼 optional sub-package 설치 가능하다.
``` sh
$ pip install `apache-airflow[aws]`
```