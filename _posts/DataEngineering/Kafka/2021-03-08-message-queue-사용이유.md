---
layout: post
title: "Message Queue 사용이유"
date: 2021-03-08 10:50:00 +0900
categories: [DataEngineering,Kafka]
---

## Message Queue를 사용하는 이유?

### 1. Performance 개선

메시지를 컨슈밍하고 프로듀싱하는 endpoint들이 서로 통신하는것이 아니라, queue를 통해서 통신한다. producer는 consumer가 처리할때까지 기다릴 필요없이 publish가능하고, consumer는 데이터가 있을때 컨슈밍할수 있다. producer와 consumer가 서로서로 기다릴 필요가 없기 때문에 data flow를 최적화 할수 있다.

### 2. 신뢰성 향상

Queue하나가 다운되더라도 다른 queue가 대신해서 데이터를 제공해줄수 있다.

### 3. Decoupling

시스템의 여러 컴포넌트들간의 의존성을 제거할수 있음.

#### 4. App을 작은단위로 나눌수 있음

여러 기능을 하나의 시스템에서 처리하기보다, 여러 시스템들이 메시지를 주고받게 하여 작은단위로 나눌수 있다. 결과적으로 각각의 시스템이 테스트하고 디버깅하고 스케일하기 쉽다.

### 5. Microservice로 이동하기 쉬움

message queue을 사용해서 microservice에게 데이터의 변경을 알릴수 있다.

## 출처
[link](https://aws.amazon.com/message-queue/benefits/)
