---
layout: post
title: "Zookeeper가 KRaft로 대체된 이유"
date: 2022-04-25 17:26:00 +0900
categories: [DataEngineering,Kafka]
---

## Zookeeper를 대체하는 이유

원래구조에서는 각각의 클러스터는 컨트롤러역할을 하는 노드가 하나씩 있었고, 이 컨트롤러는 topic, partition 로그들을 저장하고 다른 브로커들처럼 consumer/produce 요청들도 다룰뿐 아니라, broker id, rack, topic, partition, leader, ISR 정보, 클러스터 범위의 topic config, security credential와 같은 클러스터 메타데이터들도 저장한다.

![zookeeper controller broker](https://cdn.confluent.io/wp-content/uploads/zookeeper-controller-brokers.jpg)

게다가 컨트롤러 브로커를 제외한 나머지 브로커들도 Zookeeper 서버와 직접적으로 상호작용할수 있다.

위와 같은 구조에서 컨트롤러는 싱글 스레드 루프에서 모든 브로커들에게 갱신된 메타데이터 정보를 전달하는 로직을 수행한다. 그러다가 클라이언트들이 직접적으로 Zookeeper 서버와 상호작용하는 구조에서, 컨트롤러를 통해서 상호작용하도록 구조가 변경되었다. 이러한 구조 변경의 목적은 Zookeeper 서버의 읽기/쓰기 부하를 줄이기 위함이었다.

하지만 브로커수와 토픽 파티션이 증가할수록 Zookeeper가 갱신에 저장해야 하는 메타데이터들이 증가하므로 확장가능하지 않다는 문제점이 여전히 존재한다. 크게 2가지 scalability 문제점이 있을수 있다.



## Scalability 문제

### 특정 브로커를 종료해야 되는 경우

컨트롤러는 종료될 브로커가 호스팅하고 있는 토픽과 파티션 정보를 알아내서 메타데이터를 업데이트 해야하고, 새로운 파티션들에 대해 새로운 리더를 선출해야 한다. 그리고 나서 ISR 정보들을 Zookeeper에 업데이트한후 새로운 메타데이터를 나머지 브로커들에게 갱신해줘야 한다. 컨트롤러는 다음의 두가지 유형의 요청을 보내게 된다.

- `UpdateMetadata`: 모든 브로커들의 local metadata cache를 업데이트
- `LeaderAndISR`: 파티션에 대응되는 모든 리플리카들에게 새로운 리더와 ISR 정보를 업데이트

![zookeeper controller updated](https://cdn.confluent.io/wp-content/uploads/zookeeper-controller-updated.jpg)

마지막으로 컨트롤러가 브로커를 제거하고 나서야 해당 브로커를 종료할수 있다. 위에서 설명한 과정을 파티션 별로 무두 해야하기 때문에 이 과정은 시간이 많이 소요된다. 위의 작업이 수행되는 도중 브로커에 쓰기 요청이 들어온경우, 요청을 처리하지 못하고 timeout을 발생할수 있다.



### 컨트롤러 failover 상황

컨트롤러가 failover되는 상황에서, 모든 브로커들은 이 상황에 대해서 노티를 받는다. 그리고 Zookeeper에게 새로운 컨트롤러가 되기 위해서 요청을 보낸다. 이때 가장 먼저 도착한 요청이 수락된다. 문제는 새로운 컨트롤러는 모든 Zookeeper 경로에 있는 토픽 파티션 정보를 포함하는 메타데이터들을 받아와야 하고, 이 메타데이터 양은 카프카 토픽 파티션이 증가할수록 늘어나게 된다. 결과적으로 초기화 과정이 오래걸릴수 있고, 이 과정동안 파티션 리밸런싱과 같은 admin 요청들은 처리할수 없게된다.

 ![zookeeper longer unavailability](https://cdn.confluent.io/wp-content/uploads/zookeeper-longer-unavailability.jpg)



### KRaft 선택하는 이유

Zookeeper에서 모든 쓰기 데이터들이 트랜젝션 로그로 관리되는것처럼 메타데이터 로그라 불리는 메타데이터 변경 이벤트들을 기록을 하는데, 이때 데이터는 새로운 카프카 토픽에 저장된다. 이러한 방식은 오프셋 메커니즘을 사용해서 로그 순서를 보장해주고 비동기 log IO를 통해서 더 나은 퍼포먼스를 제공해준다.

또 다른 장점은 토픽을 분리하게 됨으로써 일반 카프카 로그와 메타데이터 로그를 서로 분리할수 있다는 장점이 있다. 분리함으로써 포트, request handling queue, metric, thread등을 독립적으로 사용하게 된다.

결국 작은 브로커 그룹들로 하여금 메타데이터 로그를 서로 복제할수 있게 함으로써, 특정 브로커가 죽더라도 다른 브로커에 이미 메타데이터 로그가 복제가 되어있으므로 기존방식에 비해 다운타임이 현저히 줄어들게 된다.

여기서 메타데이터 로그를 복제하는 방식에는 두가지 방법이 있다.



## 메타데이터 로그 복제 방식

### Primary-backup

위 방식은 단일 리더가 로그 쓰기 요청을 처리하고, 다른 팔로워들에게 해당 쓰기를 반영한 후, 해당 팔로워들에서 성공적으로 복제가 되면 쓰기작업을 성공으로 처리하는 방법이다.

![prmary backup log replication](https://cdn.confluent.io/wp-content/uploads/primary-backup-log-replication.jpg)



### Quorum

이 방식은 단일 리더에서 쓰기 요청을 처리하는 점은 primary-backup 방식과 동일하지만, 모든 팔로워로 부터 ack를 기다리지 않고 과반수로 부터 ack가 도착하면 쓰기 작업을 성공으로 처리한다. 

![quorum log replication](https://cdn.confluent.io/wp-content/uploads/quorum-log-replication.jpg)

카프카의 primary-backup 복제 방식과 비교해서, 복제 latency가 감소하는것이 장점이다. 

정리하면 f번 연속적인 실패를 허용하기 위해서, primary-backup 방식에서는 f+1개의 리플리카가 존재해야 하고, quorum 방식에서는 2f+1개의 리플리카가 존재해야 함을 의미한다.



## KRaft 구현방식

KRaft에서는 quorum 방식을 차용하는데 이유는 두가지이다.

- HA를 위해서 더많은 in-sync 리플리카들을 수용할수 있다.
- 메타데이터 로그 추가시 latency를 낮추는것이 중요하다.

더이상 Zookeeper 서버를 사용하지 않기 때문에 리더를 선출하기 위한 다른 프로토콜이 필요해 졌다. 새로운 프로토콜에서는 여러 리더가 여러개로 인식되지 않는 방법이 필요하고 gridlock 시나리오(장시간동안 리더가 선출되지 않는 문제)를 고려해야 한다.

### 리더 선출방식

KRaft는 기존에 존재하던 Kafka leader epoch를 사용해서 단일 epoch 내에서 하나의 리더만이 선출되도록 한다. 더 구체적으로 설명하면, 클러스터의 브로커는 leader, voter, observer 중의 하나의 role을 갖는다. leader,voter는 함께 quorum을 형성하고 복제 로그에 대한 합의를 하고 필요하면 리더를 선출하는 역할을 한다. 

여러 gridlock 시나리오(예를들어, 여러 리더 candidate들이 동시에 투표를 요청하는 상황)들을 피하기 위해서 재시도 전에 randomized backup 하는 방식을 도입 했다고 한다.



### 로그 복제 방식

리더에 있는 로그를 voter에게 복제하기 위해서 pull-based 복제방식을 사용하며, voter에서 리더에게 epoch와 offset정보를 보내서 데이터를 풀링하여 컨플릭이 생기지 않으면 그대로 로그를 복제하고, 컨플릭이 발생하면 컨플릭이 생긴 부분 데이터를 잘라내고 그다음 리더와 데이터를 동기화한다. 만약 voter들이 미리 정의된 시간내에 응답을 받지 못하면 epoch를 증가시키고 새로운 리더를 선출한다. 리더의 liveness를 판단하기 위해서 heartbeat 메커니즘을 사용한다.



### Pull vs. push-based replication

pull 방식은 실현가능한 offset으로 직접적으로 잘라낼수 있으므로, push based 방식에 비해서 라운드 트립 시간이 줄어든다. pull 기반의 KRaft는 장애가 많이 발생하는 서버들에 덜 취약한데, 그 이유는 리더가 어느 리플리카들이 voter에서 빠졌는가를 알고 있기 때문이다. pull 방식의 또 다른 장점은 Kafka의 로그 복제 레이어가 이미 pull기반의 복제로 구현이 되어있으므로, 코드를 재사용할수 있다는 점이다. 하지만 새로운 리더가 독립적인 "begin epoch" API를 호출하여 quorum을 통지해줘야 한다는 단점이 있다. 원래의 Raft 모델에서는, 이러한 노티는 리더의 push data API로 전달될수 있었다. 또한 quorum의 과반수로부터의 레코드들을 커밋하기 위해서, 리더는 voter들이 다음 fetch 요청을 보낼때까지 기다려야 한다는 문제점도 존대한다. 이러한 트레이드 오프는 diruptive server 문제를 해결하기 위해서는 어쩔수 없다.

![quorum controller](https://cdn.confluent.io/wp-content/uploads/quorum-controller.jpg)

최종적으로 Quorum Controller는 위에서 설명한 KRaft 프로토콜을 기반으로 구현되었다.



### 결론

- 메타데이터를 이벤트 로그들로 유지하는것은 더 효율적이다.
- 메타데이터 로그를 기반으로 Quorum 컨트롤러를 구현할때, 단일 카프카 클러스터에서 수백만의 파티션들로 인해 발생하는 확장성문제를 해결할 수 있다.

## 출처 : [Why ZooKeeper Was Replaced with KRaft – The Log of All Logs](https://www.confluent.io/blog/why-replace-zookeeper-with-kafka-raft-the-log-of-all-logs/?utm_source=linkedin&utm_medium=organicsocial&utm_campaign=tm.devx_ch.bp_why-zookeeper-was-replaced-with-kraft-log-of-all-logs_content.apache-kafka)
