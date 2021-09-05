---
layout: post
title: "pip install에 대하여"
date: 2021-09-04 12:51:00 +0900
categories: [Language,Python]
---

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
