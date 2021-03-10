---
layout: post
title: "[ROAD TO DATA ENGINEER] Kafka Basic Concepts"
date: 2020-10-06 +0900
categories: [DataEngineering,Kafka]
---
# Why do we use Kafka?
## Without Kafka
![img](/assets/img/post/Kafka/2020-11-06-withoutKafka.png)
## With Kafka
![img](/assets/img/post/Kafka/2020-11-06-withKafka.png)

# Topic
- 특정한 data stream
  - database의 테이블과 비슷한 개념
  - 원하는 만큼 생성가능
  - 이름으로 구분됨(identified by name)
- Topic들은 partition으로 나누어짐
  - 각각의 파티션은 정렬되어있음
  - partition 내에 있는 메시지들은 offset이라 불리는  incremental한 아이디를 가진다. ( partition 0, partition 1, ... )

![img](/assets/img/post/Kafka/2020-10-06-KafkaTopic.png)

- Offset은 오직 specific partition에서 의미가 있음.
- partition 내에서만 순서가 존재함(partition 간에는 순서가 보장되지 않음)
- Data가 제한된시간 (기본 1주)내에 존재함
데이터가 partition에 써지면, 바꿀수없음(immutability)

# Brokers
- Kafka cluster는 broker(servers)들로 구성되어있다.
- broker들은 id로 구분
- 각각의 브로커는 특정 topic partition들을 가지고 있음
- 아무 브로커에게 연결되면 (called a bootstrap broker), 전체 클러스터에 연결됨

![img](/assets/img/post/Kafka/2020-10-06-broker.png)

- Topic-A는 3개의 파티션, Topic-B는 2개의 파티션을 가지고 있음.

# Topic replication factor

- broker가 down되어도 다른 broker가 계속 데이터를 서빙할수있음.

![img](/assets/img/post/Kafka/2020-10-06-broker2.png)

- 위 경우는 replication factor가 2인경우이다.
- 특정 한 partition에는 하나의 broker만이 leader가 될수 있다.
- 그 leader만 data를 주고 받을 수 있다.
- 다른 broker들은 leader의 데이터를 동기화한다.
이때 다른 broker들을 ISR(In-Sync-Replica)라고 부른다.

# Producers

- ack=0: Producer는 ack를 기다리지 않는다.(data 손실가능)
- ack=1: Producer는 leader에대한 ack를 기다린다.(limited 데이터 손실)
- ack=all : Leader + replicas의 ack를 기다린다(data 손실 없음)
- Message Keys : key를 세팅해놓으면 특정 키에 해당하는 데이터들은 같은 partition에 저장된다
- key를 따로 세팅해두지 않으면 round robin 으로 broker 101, 102, 103 차례대로 데이터가 저장된다. (즉, 임의의 partition에 저장된다.)

# Consumers

- Consumer들은 topic에 있는 데이터들을 읽는다.
- 어느 broker를 읽어야하는지 알고있다
- 또한 broker가 down됬을시 어떻게 대처할지도 알고있음.
- Data는 partition내에서만 순서대로 읽어진다.

# Consumer Group

- 보통 하나의 application 단위를 Consumer Group이라고 한다
- Consumer Group에 있는 Consumer들은 서로 다른 partition들을 읽어들인다.
- partition 수보다 Consumer의 수가 더많으면, 몇몇 Consumer는 비활성화된다.

# Consumer Offsets

- Kafka는 Consumer group이 읽은 offset을 저장한다.
- offset은 Kafka topic에 __consumer_offsets라는 이름을 저장된다.
- consumer가 데이터를 처리하고 나면 offset을 kafka에 commit 한다.
- consumer가 down되면 읽었던 부분부터 다시 읽어들일 수 있게 하기 위함이다.

# Delivery Semantics for consumers
- Consumer들은 언제 offset을 커밋할지 선택할수있다.
  - At most once 
    - message가 수신되자 마자 커밋
    - processing이 잘못되면 message가 유실됨(다시 읽을 수 없음)
  - At least Once (보통 선호됨)
    - 데이터가 처리되고나서 커밋
    - 처리가 잘못되면, 다시 읽음
    - 같은 메시지를 여러번 처리할수 있기 때문에, processing이 idempotent(연산을 여러 번 적용하더라도 결과가 달라지지 않는 성질)하도록 해야함
  - Exactly Once
    - 프로듀서가 같은 메시지를 여러번 전달하더라도, end consumer에게는 정확히 한번만 전달되도록 함.
    - 프로듀서,브로커,컨슈머가 모두 협력해야 가능하다. 예를들어, 컨슈머를 이전 offset으로 리와인드 하게 되면, 해당 offset에서 최신 offset으로의 메시지를 다시 컨슘하게 된다.

# Kafka Broker Discovery

- Kafka broker들은 bootstrap server라고 불리는데, 오직 하나의 broker에만 연결되면 된다는 의미이다. 하나의 broker에 연결되면 전체 클러스터에 연결된다.

- 개별 broker는 모든 broker들에 대한 정보와 topic, partition들에 대한 정보를 가지고 있다.

# Zookeeper

- broker들을 관리함
- partition들에 대한 leader 선출을 수행하는데 도움을 줌
- new topic, broker dies, broker comes up, delete topics 등과 같은 정보들을 Kafka에게 알려줌
- Kafka는 Zookeeper없이는 작동할수 없음.
- Zookeeper는 홀수개의 서버로 동작함.
- Zookeeper에는 leader와 follower가 있는데, leader는 write를 담당하고 follower들은 read를 담당함.
- consumer offset은 Kafka topic에 저장되고 Zookeeper에는 더이상 저장되어있지 않음.