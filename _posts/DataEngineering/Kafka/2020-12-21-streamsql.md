---
layout: post
title: "StreamSQL"
date: 2020-12-21 22:33:00 +0900
categories: [DataEngineering,Kafka]
---

## StreamSQL
실시간 데이터 스트림을 처리가 가능한 SQL을 확장한 쿼리 언어이다. SQL은 주로 테이블을 다루는 용도이지만, StreamSQL은 스트리밍 데이터를 처리하는 능력까지 갖고있다. 스트림 데이터에대한 쿼리는 지속적으로 증가하는 결과값이 리턴된다.

## 세부적인 연산들

- **SELECT** - 스트림에 있는 데이터를 대상으로 함수를 계산하거나 원치않는 튜플들을 걸러낼수 있음.

- **JOIN** - 테이블과 스트림데이터를 조인하는 기능.

- **UNION,MERGE** - 두개이상의 스트림 데이터를 대상으로 합집합 또는 Merging가능.

- **Windowing and Aggregation** - 예를들어 5분안에 들어온 스트림데이터들을 하나의 배치로구성하여, count,average,max와 같은 집계함수를 적용할수 있음.

- **Windowing and Joining** - 여러 스트림들을 윈도잉(특정 구간 데이터를 하나로 묶기)하여 함께 조인가능

## KSQL

> 아파치 카프카를 위한 스트리밍 SQL엔진

- 자바나 파이선 코드작성 없이 간단한 SQL로 스트림 처리를 가능하게 함.

- Confluent가 프로그래밍 스킬이 없는 사람들도 데이터 처리를 가능하도록 하기 위해서 개발

- data filtering, transformations, aggregations,joins,windowing,sessionization과 같은 스트리밍 연산들을 제공

### 작동방식

![image](https://d2hhs94aauusoe.cloudfront.net/wp-content/uploads/2020/07/KSQL03.png)

KSQL 서버는 카프카를 대상으로 쿼리를 실행할수 있는 프로세스이다. 더 많은 processing power를 원하면 KSQL 서버의 인스턴스를 더 만들면 된다. 이 인스턴스들은 falut-tolerant하며, 하나의 인스턴스가 다운되면 다른 인스턴스가 작업을 이어받을수 있다. 

### Kafka Streams vs KSQL

![image](https://d2hhs94aauusoe.cloudfront.net/wp-content/uploads/2020/07/KSQL04-1536x864.png)

KSQL은 Kafka Streams를 기반으로 구현되었다. KSQL은 간단한 방법으로 데이터를 얻고 처리할 필요가 있는 사람들에게 적합하다. 만약, 데이터 스트림을 처리하는데 더 복잡한 작업이 필요하다면, Kafka Streams를 이용해서 프로그래밍 하는것이 좋다. 