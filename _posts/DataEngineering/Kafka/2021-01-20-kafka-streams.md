---
layout: post
title: "Kafka Streams"
date: 2021-01-20 19:09:00 +0900
categories: [DataEngineering,Kafka]
---

## Kafka Streams

- Kafka Streams API로 Java Application 개발 가능

![img](https://docs.confluent.io/5.2.0/_images/streams-introduction-your-app.png)

## Stream Concepts

### Stream 

unbounded(unknown, unlimited size), 지속적으로 업데이트 되는 데이터 셋을 말한다. 카프카 토픽처럼 하나이상의 **stream partition**으로 구성된다.

**stream partition** 이란 ordered,replayable, fault-tolerant한 변경불가능한 **data record**들의 순서이다. **data record** 는 key-value 쌍으로 정의된다.



### Stream Processing Appliation

Kafka Streams를 사용하는 모든 프로그램을 말한다. broker에서 동작하는것이 아니라 독립적인 JVM 인스턴스 또는 독립적인 클러스터로 동작한다.

![img](https://docs.confluent.io/5.2.0/_images/streams-apps-not-running-in-brokers.png)

**application instance** 는 실행중인 인스턴스 또는 어플리케이션의 사본을 말한다. Application instance들은 아래와같이 각각의 머신에서 실행이 가능하고, data processing 작업을 자동으로 협력하는 방식으로 되어있다.

![img](https://docs.confluent.io/5.2.0/_images/scale-out-streams-app.png)

### Processor Topology

