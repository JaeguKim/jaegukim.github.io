---
layout: post
title: "Schema Evolution"
date: 2021-02-25 10:10:00 +0900
categories: [DataEngineering,Kafka]
---

### Kafka Avro Serializer

![Image for post](https://miro.medium.com/max/2052/1*OortllduCOkKV6_s4dZ6fg.png)

* 순서
  1. Producer는 메시지를 직렬화 하기 위해 KafkaAvroSerializer를 사용
  2. kafkaAvroSerializer는 SchemaRegistryClient라는 것을 사용하여 Schema Registry에 스키마정보를 등록
  3. Schema Registry에 정상적으로 스키마가 등록되면 SchemaID를 반환
  4. KafkaAvroSerializer는 SchemaID와 메시지 본문을 포함한 데이터를 직렬화 함
     * 직렬화 구조 : Magic Byte (1byte) + SchemaID(4byte) + Data
     * 다른 Confluent Schema Registry가 앞 5바이트를 포함해서 전달하지는 않음

## Confluent Schema Registry

> 아파치 카프카와 더불어 다양한 플랫폼들을 연결시켜주는 오픈소스

* RESTful 인터페이스 사용
* 스키마를 관리하거나 조회하는 기능을 제공
* Producer, Consumer는 Apache Avro 포맷 메시지를 Kafka를 통해 전달하고 받음
* 받는 순서

![Image for post](https://miro.medium.com/max/1904/1*6crlNRdKaB7B1P82rE10UQ.png)

1. Consumer는 Kafka로 부터 바이너리 데이터를 받는데 이 데이터에는 스키마 ID가 포함되어 있음
2. 해당 ID를 가지고 로컬 캐시 혹은 Confluent Schema Registry에서 스키마 정보를 탐색하여 가져오고, 스키마 정보를 사용해 역직렬화를 함



### 스키마 진화 전략

* Backward : 새로운 스키마로 이전 데이터를 읽는 것
  * 새로운 스키마 필드에 해당 필드에 default value가 없으면 오류 발생
  * 새로 추가되는 필드에 default value를 지정할 때에만 스키마 등록이 허용
  * Confluent Schema Registry는 기본적으로 Backward로 동작
* Forward : 이전 스키마에서 새로운 데이터를 읽는 것
  * 새로운 스키마에서 특정 필드가 삭제된다면, 해당 필드는 이전 스키마에 default value를 가지고 있어야함
* Full : Backward, Forward를 모두 만족하는 것 (추천)
* None : Backward, Forward 둘다 만족하지 못하는 것

### Schema Registry 장단점

* 장점
  * 안전성 - 스키마 레지스터리가 잘못되면 카프카에 메시지를 전달하지 않음
  * 카프카에 전달되는 바이너리 데이터에 스키마 정보가 포함되어 있지 않기 때문에 상대적으로 적은 용량의 데이터가 전달
  * 따라서 json등과 비교하여 카프카 시스템에서 더 적은 공간을 차지하고 네트워크 대역폭도 절약할 수 있음
* 단점
  * 스키마 레지스터리에서 장애가 발생하면 정상적으로 메시지 전달이 x
  * 카프카와 비교했을 때 운영포인트가 증가
  * Avro 포맷은 Json과 비교했을 때 직렬화과정에서 퍼포먼스가 조금 떨어짐 (하지만 크게 떨어지지는 않음)

### Client 업그레이드 순서

> compatibility type에 따라서 클라이언트를 업그레이드 해야하는 순서가 있다.

- ```BACKWARD``` or ```BACKWARD_TRANSITIVE``` : 모든 컨슈머를 새로운 이벤트를 처리하기전에 업그레이드 해야함. (예전 스키마를 사용해서 새로운 스키마 데이터를 못읽으므로)

- ```FORWARD``` or ```FORWARD_TRANSITIVE``` : 모든 프로듀서를 먼저 업그레이드 해야함. 예전 스키마 데이터가 컨슈머에게 이용이 불가능하도록 해야함. 그리고나서 컨슈머를 업그레이드 함.

- ```FULL``` or ```FULL_TRANSITIVE``` : 컨슈머가 새로운 스키마데이터를 읽을수도 있고 예전 스키마 데이터를 읽을수도 있다. 그러므로 컨슈머와 프로듀서를 독립적으로 업그레이드 할수 있다.

- ```NONE``` : compatibility 체크가 비활성화 되어있다. 그러므로 클라이언트를 업그레이드 할때 주의해야 한다.

## 참고

| Compatibility Type | Changes allowed | Check against which schemas | Upgrade first
| -- | -- | -- | --
| ```BACKWARD``` | - Delete fields, Add Optional fields(새로운 스키마에서 Default 값이 설정된 필드만 추가가능) | Last version | Consumers
| ```BACKWARD_TRANSITIVE``` | - Delete fields, Add optional fields | All previous versions | Consumers
| ```FORWARD``` | - Add fields, Delete Optional fields(이전 스키마에서 Default 값이 설정된 필드만 삭제가능) | Last version | Producers
| ```FORWARD_TRANSITIVE``` | - Add fields, Delete Optional fields | All previous versions | Producers

