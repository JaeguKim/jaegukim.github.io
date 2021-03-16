---
layout: post
title: "Data Processing Architecture"
date: 2021-03-10 14:59:00 +0900
categories: [DataEngineering,Concept]
---

## Data Processing Architecture

### Lambda Architecture

traditional batch 파이프라인을 fast real-time stream pipeline을 결합하기 위해서 사용하는 data processing을 위한 deployment model. 

![The Lambda Architecture contains both a traditional batch data pipeline and a fast streaming pipeline for real-time data, as well as a serving layer for responding to queries.](https://hazelcast.com/wp-content/uploads/2020/04/19_Lambda.png)

#### Data Sources

데이터가 동시에 batch layer와 speed layer에 전달된다.

#### Batch Layer

데이터는 immutable, append-only로 간주된다.

#### Serving Layer

점진적으로 최근 batch view을 인덱싱한다. 인덱싱 작업이 수행되고 있는 동안에 새롭게 도착한 데이터가 큐에서 대기하게 된다.

#### Speed Layer(Stream Layer)

가장 최근에 추가된 데이터를 인덱싱한다. 이 데이터는 현재 색인중인 데이터 뿐만 아니라 현재 인덱싱중인 데이터보다 최근 데이터도 포함한다. 이 레이어는 stream processing 기술을 사용하여 들어오는 데이터를 실시간으로 인덱싱한다. 주로 Apache Storm, Apache Flink, Spark Streaming 기술이 사용된다.

#### 장점

최신데이터는 Speed Layer에서 조회하고, historical 데이터는 Batch Layer에서 조회함으로써 쿼리시간을 줄일수 있다.

#### 단점

스피드 레이어와 배치 레이어가 모두 똑같은 처리를 구현하고 있으므로 중복된 비즈니스 로직 및 두 경로의 아키텍쳐 관리에 따른 복잡성 증가

### Kappa Architecture

streaming data를 처리하기위해 사용되는 아키텍쳐이다. 한가지 기술 스택으로 batch processing과 real time processing을 처리할수 있다. stream processing engine이 유일한 데이터 transformation engine이다.

![Kappa Architecture Diagram](https://hazelcast.com/wp-content/uploads/2020/01/30_KappaArchitecture.png)

#### 장점

하나의 기술 스택으로 stream processing, batch processing 가능

## 출처

[https://jhleed.tistory.com/122](https://jhleed.tistory.com/122)

[https://hazelcast.com/glossary/kappa-architecture/](https://hazelcast.com/glossary/kappa-architecture/)