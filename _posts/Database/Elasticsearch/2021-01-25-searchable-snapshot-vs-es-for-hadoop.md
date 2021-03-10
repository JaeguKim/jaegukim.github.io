---
layout: post
title: "Searchable snapshot vs es for hadoop"
date: 2021-01-25 11:21:00 +0900
categories: [Database,Elasticsearch]
---

## Searchable Snapshot

### Snapshot

snapshot이란 실행중인 Elasticsearch cluster에 대한 백업이다. 모든 데이터 스티림, 인덱스들을 포함하여, 전체 클러스터에 대한 스냅샷을 생성가능하다. 특정 데이터 스트림 또는 인덱스에대한 스냅샷또한 생성가능하다.

스냅샷을 생성하기전에 snapshot repository를 등록해야한다. 스냅샷은 로컬 또는 원격 저장소에서 저장이 가능하다. 원경저장소는 Amazon S3, HDFS, Microsoft Azure, Google Cloud Storage와 그리고 다른 플랫폼들에서 저장가능하다. 

### 스냅샷의 장점

Elasticsearch는 스냅샷을 점진적으로 저장한다 : 스냅샷 process는 이전의 스냅샷에서 복사되지 않은 데이터들만 원격저장소로 복사한다. 이를 통해 불필요한 공간의 낭비를 줄일수 있다. 이를 통해, 최소한의 오버헤드로 매우 빈번한 스냅샷 생성이 가능해진다. 이러한 점진성은  하나의 저장소내에서만 적용이된다. 왜냐하면 저장소들간에는 아무런 데이터도 공유되지 않기 때문이다. 스냅샷들은 또한 서로 논리적으로 독립적이고, 이는 같은 저장소내에서도 적용된다 : 스냅샷을 삭제하는것은 다른 스냅샷의 integrity에 영향을 주지 않는다.

### HDFS로 저장하는법

- HDFS Repository Plugin
- Apache Hadoop 2.x (현재 2.7.1) 을 대상

## Elasticsearch for Apache Hadoop

- Hadoop job(Map/Reduce, Hive, Pig, Spark, Storm)에서 Elasticsearch와 상호작용(양방향 데이터 송수신)할수 있게 하는 라이브러리
- Hadoop job들이 Elasticsearch를 사용하는것이 하둡 클러스터내에 있는 자원을 사용하는것처럼 사용할수 있도록 해줌
- elasticsearch-hadoop 이라는 용어로도 사용됨

### 주된 특징

#### Scalable Map/Reduce model

Elastic search-hadoop의 모든 작업은 여러 하둡 테스크들로 나누어지고(타깃 샤드의 수에 기반), 각각의 테스크가 병렬로 Elasticsearch와 상호작용

#### REST based

Elastic search-hadoop은 Elasticsearch REST interface를 사용, 유연한 deployment를 허락하고 네트워크상에서 포트의 수를 최소화 

#### Self contained

라이브러리는 용량이 작고 빠름. 300KB 라이브러리 제외하고 추가 종석성 없음, 클러스터내에 elasticsearch-hadoop을 분배하는것은 간단하고 빠름

#### Universal jar

vanilla Apache Hadoop이든 특정 버전 하둡이든 elasticsearch-hadoop 라이브러리 실행가능

#### Memory, I/O efficient

Pull-based parsing, bulk update, 네이티브 타입 변환작업이 메모리, 네트워크 I/O 관점에서 효율적

#### Adaptive I/O

전송에러발생시 자동 재전송, Elasticsearch 노드 장애시, 이용가능한 노드로 리퀘스트

#### Facilitates data co-location

Elasticsearch-hadoop은 네트워크 접근 정보를 노출하므로써,  같은 클러스터에 위치한 Elasticsearch 와 하둡 클러스터가 서로를 인지하도록 함. 이는 network IO를 감소시킨다.

#### Apache Hive 지원

Elasticsearch를 대상으로 Hive 쿼리 실행가능. elasticsearch-hadoop은 Elasticsearch를 Hive table처럼 사용할수 있도록 지원.

#### Apache Spark

데이터를 스트리밍 하거나 임의의 RDD를 인덱싱함으로써, Elasticsearch 대상으로 빠른 변환을 실행가능. Java와 Scala 둘다 지원

#### Apache Storm

Elasticsearch를 ```Spout```(source) 또는 ```Bolt```(sink) 로 사용할수 있게함.

## 출처

[Snapshot and restore](https://www.elastic.co/guide/en/elasticsearch/reference/master/snapshot-restore.html)

[Snapshot/Restore Repository plugins](https://www.elastic.co/guide/en/elasticsearch/plugins/master/repository.html)

[Elasticsearch for Apache Hadoop](https://www.elastic.co/guide/en/elasticsearch/hadoop/current/reference.html)

