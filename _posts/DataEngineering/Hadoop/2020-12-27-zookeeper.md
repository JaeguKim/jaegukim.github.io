---
layout: post
title: "Zookeeper"
date: 2020-12-27 19:18:00 +0900
categories: [DataEngineering,Hadoop]
---

## Zookeeper

- 클러스터내에서 동기화되어야하는 정보들을 기록

  - 어느 노드가 마스터인가?
  - 작업들이 어느 워커에 할당되어있는가?
  - 현재 이용가능한 워커는 무엇인가?
- 클러스터내에 partial failure를 회복시키기 위해 사용가능
- HBase, High-Availability MapReduce, Drill, Storm 등을 통합시킬수 있는 부분

### Failure modes

- 마스터 노드가 크래시 되면, 워커노드중에 마스터노드를 선출해야함

- 워커노드가 크래시되면, 작업을 다시 재분할 해야함

- 네트워크문제가 발생하면 클러스터의 일부분이 나머지를 볼수 없게됨

### 분산시스템에서 "Primitive" 작업들수행

- 마스터 선출

  - 하나의 노드가 자신을 마스터로 등록하고, 그 정보에 락을 건다.
  - 다른 노드들은 그 락이 해제될때까지 마스터노드가 될수 없다.
  - 오직 하나의 노드만 락을 가질수 있다.

- 크래시 감지

- Group 관리 - 어떤 워커가 이용가능한가

- 테스크 할당 

### 아키텍처

![img](https://jaegukim.github.io/assets/img/post/Hadoop/zookeeper.png)  

- Zookeeper Ensemble이 Zookeeper데이터들을 복제

- 설정에 따라서  Split Brain Problem발생가능

