---
layout: post
title: "Kafka Trouble Shooting"
date: 2020-12-04 23:35:00 +0900
categories: [DataEngineering,Kafka]
---

## The process cannot access the file because it is being used by another process.

위 경우는 다른 카프카가 이미 해당 파일을 사용하고 있기 때문에 발생한다. 가장 빠른 방법은 카프카 포트번호(default 9092)를 사용중인 카프카를 종료시키고 재실행하는 것이다.
즉, 9092 포트를 사용중인 프로세스를 종료시키면된다. 

```
sudo lsof -t -i tcp:9092 | xargs kill -9
```

## Unknown error fetching data for topic-partition

kafka-python python package가 카프카 브로커 버전 2.5버전과 호환이 되지 않아서 문제가 발생하였다. 21년 12월기준 kafka-python 패키지는 카프카 2.4버전까지만 지원한다.

- 해결방법 : confluent_kafka 모듈을 사용하도록 변경