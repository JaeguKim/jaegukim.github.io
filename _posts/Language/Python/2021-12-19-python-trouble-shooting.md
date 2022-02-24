---
layout: post
title: "[Python] trouble shooting"
date: 2021-12-19 14:37:00 +0900
categories: [Language,Python]
---

## OSError: mysql_config not found when installing ```mysqlclinet```
- solution : install mysql on your mac by ```brew install mysql```

## `pip install cryptography` 설치시 에러 발생
운영체제별로 다음 [실행과정](https://cryptography.io/en/3.4.8/installation.html) 수행

## [error 32] broken pipe 에러
kafka producer app에서 prometheus로 쿼리를 할때 prometheus에서 설정해둔 request timeout값을 넘긴 경우, prometheus에서 connection을 close하게 되고 결과적으로 클라이언트에서 broken pipe에러를 보게되는것으로 추정된다.

## Can't open file when open file with write mode

open의 path 파라미터에 디렉토리가 포함되어 있는경우, 해당 디렉토리가 반드시 존재해야 오류가 나지 않는다. `open(path,'w')` 를 실행했을때 해당 path에 파일이 존재하지 않으면 해당 파일이 생성이 된다. 하지만 디렉토리가 새로 생기진 않는다.

## Error "cannot schedule new futures after interpreter shutdown" while working through treading

main thread에서 다른 스레드를 기다리지 않을 때 발생한다. 따라서 join함수를 반드시 호출해야 한다.

``` python
import threading
import boto3

class worker (threading.Thread):
    terminate = False
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        # make BOTO3 CLIENT
        s3_client = boto3.client(...)
        while not self.terminate:
            # BOTO3 downloads from global list, not shown in this code
            s3_client = boto3.download_file(...)
    def stop(self):
        self.terminate = True

mythread = worker()
mythread.start()
# **************** THIS IS IMPORTANT
mythread.join()
# **************** /THIS IS IMPORTANT
```

## asyncio 사용중 "got Future <Future pending> attached to a different loop"
하나의 event_loop 안에서 다른 event_loop에서 바인딩된 함수를 호출해서 발생하였다. 하나의 event_loop안에서 함수를 호출하도록 변경해주었다.

## Docker container에 Prophet package 설치 오류

Docker image 빌드시 prophet 설치과정에서 아래의 에러가 발생했다. 에러발생에도 불구하고 이미지 빌드는 성공을 해서 빠르게 대응을 하지 못했다.

``` 
...
from convertdate.islamic import from_gregorian, to_gregorian
      ModuleNotFoundError: No module named 'convertdate'
...
```

컨테이너에 접속해서 Prophet 패키지를 수동으로 설치하려고 시도했을때는 또 `COMPILING THE C++ CODE FOR MODEL anon_model` 에러가 발생하여, Debian linux에서 gcc 컴파일러가 설치되지 않아서 생긴 이유라고 짐작을 하기도 했다. 하지만 Debian에는 gcc 컴파일러가 이미 잘 설치가 되어있었고, 결국 구글링을 해보다가 pystan 패키지가 잘 동작하는지 검사해보라는 조언이 있어서, 샘플코드를 돌려보니 역시나 돌아가지 않았다. 결국 아래와 같이 해결하였다.

``` Dockerfile
RUN pip3 install --no-cache-dir convertdate==2.3.0 lunarcalendar==0.0.9 holidays==0.10.3 cython==0.29.21 pystan==2.19.1.1 pandas==0.23.4 && \
    pip3 install --no-cache-dir -r $SPARK_HOME/conf/requirements.txt
```

여기서 처음에는 covertdate, lunarcalendar 등 미리 설치되어야 하는 패키지들을 requirements.txt 파일에서 순서의 앞단에 배치하도록 하였으나, 패키지들의 설치순서는 정의 순서와 관계가 없다는 점을 깨달았다. 결국 위 처럼 명시적으로 설정하여 설치했다.
