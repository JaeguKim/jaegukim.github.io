---
layout: post
title: "Logical Replication"
date: 2021-01-06 23:11:00 +0900
categories: [Database,PostgreSQL]
---

## Logical Replication

replication identity(보통은 primary key) 에 기반하여, 데이터 오브젝트들과 그것들의 변화를 복제하는 방법을 말한다. 정확한 block 주소, byte-by-byte replication을 사용하는 physical replication과는 비교되는 개념이다. PostgreSQL은 physical,logical replication 둘다를 병렬적으로 지원한다. Logical replication은 data replication과 보안에 높은 수준의 통제를 허락한다.

Logical replication은 publisher node에대한 여러 publication을 구독하는 여러 subscriber들을 가진 publish and subscribe model을 사용한다. Subscriber들은 그들이 구독하는 publication들로부터 데이터를 받아올수 있고 연속해서 데이터를 re-publish함으로서 cascading replication 또는 더 복잡한 설정들을 할수 있다.

Logical replication은 전형적으로 publisher database에 있는 데이터의 스냅샷을 구한다음 subscriber에게 복사한다. 복사가 끝나면, publisher에 있는 변화들이실시간으로  subscriber에게 보내진다. subscriber는 publisher와 같은 순서로 데이터를 적용하며 결과적으로 하나의 subscription내에서 transactional consistency가 보장된다. 이 방식은 때때로 transactional replication이라고 부르기도 한다.

Subscriber database는 다른 PostgreSQL 인스턴스와 같은 방식으로 행동하며 자신만의 publication을 정의함으로써 다른 데이터베이스들에 대하여 publisher로 사용되어 질수 있다. Subscriber가 read only application 으로 취급될때는 하나의 subscription에서 conflict가 발생하지 않는다. 반면에 어플리케이션이나 다른 subscriber들에 의해서 데이터가 write된다면 conflict가 발생할수 있다.

### Publication

**publication**은 physical replication master에 정의가 가능하다. **publication**이 정의되어있는 노드를 **publisher**라한다.  **publication**은  하나이상의 테이블들에서 발생한 일련의 변화들이며, **change set** 또는 **replication set** 이라고도 한다. 하나의 **publication** 은 오직 하나의 데이터베이스에만 존재한다.

각각의 테이블은 필요하면 여러 **publication**에 추가될수 있다. **publication** 은 현재 테이블만 포함할수 있다. **publication** 은 ```INSERT```, ```UPDATE```, ```DELETE``` 의 조합으로 생산되는 변화들을  제한할수 있다. published table은 ```UPDATE```, ```DELETE``` 작업을 복제하기 위해 **replica identity** 를 가져야만 한다. 이러한 과정의 결과로 subscriber 측에서 update,delete할 행들을 식별할수 있게된다. default로 이 값은 primary key이다. unique index또한 **replica identity** 로 설정이 가능하다. 테이블에 적절한 키가 없다면, **replica identity** 는  **full** 로 설정이 되게되며, 하나의 행전체가 키가 됨을 의미한다. 이는 성능상 비효울적이며 다른 해결책이 없을때만 사용되어야 한다. publisher side에서 replica identity가 **full**로 설정이 되어있다면 subscriber side에는 같거나 더 적은수의 칼럼들을 구성하는 replica identity만이 설정되어야한다. replica identity가 설정되지 않은 테이블이 **publication** 에 추가된다면 ```UPDATE``` or ```DELETE``` 작업들은 publisher에서 에러를 발생시킨다. ```INSERT``` 작업들은 replica identity와 관계없이 진행이 가능하다.

### Subscription

logical replication에서  downstream side이다. subscription이 정의되있는 노드를 **subscriber** 라 한다. subscription은 또다른 데이터베이스에 대한 연결과 구독하고자 하는 publications들을 정의한다. subscriber database는 다른 PostgreSQL 인스턴스와 같은 방식으로 동작하며 다른 데이터베이스들에 대한 publisher로도 사용될수 있다. 

subscriber node는 여러 subscription들을 가질수 있으며 달일 publisher-subscriber pair간에도 여러 subscription을 가질수 있다. 이 경우 subscribed publication object들이 서로 겹치지 않도록 주의해야한다. 하나의 subscription은 하나의 replication slot을 통해서 변화를 받을것이다. 추가적인 임시 replication slot들은 이미 존재하는 테이블 데이터의 초기 동기화에 필요할수 있다.

## 출처

[https://www.postgresql.org/docs/10/logical-replication.html](https://www.postgresql.org/docs/10/logical-replication.html)