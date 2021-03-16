---
layout: post
title: "Apache Flink vs Apache Spark"
date: 2021-03-05 23:50:00 +0900
categories: [DataEngineering,Concept]
---

## Apache Flink vs Apache Spark

| Features | Apache Flink | Apache Spark
| -- | -- | --
| Computation Model | operator 기반 computational model | micro-batch 기반 model
| Streaming Engine | 모든 작업에 대해서 stream을 사용 : streaming, SQL, micro-batch, batch. Batch는 finite set of streamed data | 모든 작업에 대해서 micro-batch를 사용함. 실시간 데이터 스트림을 실시간으로 처리하기는 어려움 
| Iterative processing | 두가지 dedicated iteration 작업을 제공 : Iterate, Delta Iterate | non-native iteration에 기반하는데, Spark이 아닌 다른 시스템의 일반 for loop으로 구현이 되어있다. 
| Optimization | 실제 프로그래밍 인터페이스와는 독립적인 optimizer를 갖고 있다. | Spark job은 수동으로 Optimize 되어야한다. 
| Latency | 최소한의 configuration설정으로, low latency, high throughput을 달성할수 있다. | Apache Flink와 비교하여 높은 latency를 가진다.
| Performance | 다른 데이터 프로세싱 시스템보다 훌륭한 성능을 나타낸다. closed loop iteration operator를 사용하는데, maching learning과 graph processing을 더 빠르게 한다. | Micro-batch를 사용하다보니 Flink보다 효율적이지 못하다.
| Fault tolerance | Chandy-Lamport distributed snapshot에 기반을 둔 fault tolerance mechanism. 경량 메커니즘이고 high throughput과 강한 consistency를 보장한다. | exactly once semantic을 보장한다.
| Flink는 record-based 또는 custom user-defined window criteria 제공 | time-based window criteria 제공
| Memory Management | automatic memory management를 제공 | configurable memory management 제공. Spark 1.6부터는 자동화된 memory 관리도 제공