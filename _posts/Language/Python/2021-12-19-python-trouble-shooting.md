---
layout: post
title: "[Python] trouble shooting"
date: 2021-12-19 14:37:00 +0900
categories: [Language,Python]
---

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