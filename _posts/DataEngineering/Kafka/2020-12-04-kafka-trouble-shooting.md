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

## kafka-python 패키지에서 Unknown error fetching data for topic-partition

kafka-python python package가 카프카 브로커 버전 2.5버전과 호환이 되지 않아서 문제가 발생하였다. 21년 12월기준 kafka-python 패키지는 카프카 2.4버전까지만 지원한다.

- 해결방법 : confluent_kafka 모듈을 사용하도록 변경

## confluent_kafka 패키지에서 Local: Queue full

confluent_kafka 내부의 internal queue사이즈가 가득찬 경우 발생한다. 주로 `poll([timeout])` 함수를 호출하지 않아서 발생한다.

> `poll([timeout])` 함수는 메시지를 카프카 브로커에 전달하고 결과정보를 > callback함수를 통해서 전달하는 역할을 한다.
> `flush[timeout]` 함수는 프로듀서 큐에 있는 모든 메시지가 브로커에 전달될때까지 대기한다. 파라미터에 timeout값을 전달하지 않으면 `len()`값이 0이 될때까지 `poll()`함수를 호출하며, timeout값을 전달하면 해당 값동안 `poll()`함수를 호출한다. 결과값으로 queue에 남아있는 메시지수를 리턴한다.

## COMMIT Failed error

주로 Kafka Rebalancing 도중에 commit 요청이 들어올경우 다음의 에러가 발생한다.

- `Error: KafkaError{code=UNKNOWN_MEMBER_ID,val=25,str="Commit failed: Broker: Unknown member"}`

- `Error: KafkaError{code=NOT_COORDINATOR,val=16,str="Commit failed: Broker: Not coordinator"}`

- `Error: KafkaError{code=COORDINATOR_LOAD_IN_PROGRESS,val=14,str="Commit failed: Broker: Coordinator load in progress"}`

