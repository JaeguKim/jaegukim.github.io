---
layout: post
title: "Log Compaction"
date: 2021-03-13 12:23:00 +0900
categories: [DataEngineering,Kafka]
---

## Log Compaction

Kafka는 시간,크기에 따라서 예전 로그들을 삭제할수 있다. 카프카는 또한 record key에 대한 log compaction도 지원한다.Log compaction 이란 레코드의 최근 버전만 유지하고 이전 버전은 삭제하는 것을 말한다.

## 구조

log는 head와 tail을 가지고 있다. compacted log의 head는 전통적인 카프카 로그와 같다. 새로운 레코드들이 head의 끝에 append 된다. 모든 log compaction은 log의 tail에서 작동한다. 오직 tail만이 compact된다. 

![img](https://miro.medium.com/max/624/1*Rq8qGwHu2hYDCvsuM5mDSA.png)

## Log Compaction 과정

![Kafka Log Compaction Process](https://miro.medium.com/max/624/1*zJfxuBfEw-OrRM6qEpmpzQ.png)

## Log Compaction Cleaning

```min.compaction.lag.ms``` 는 메시지가 compact되기전 지나야 하는 최소한의 시간을 의미한다. Log compaction은 절대 메시지의 순서를 바꾸지 않고 단지 몇개를 삭제한다. Partition offset 또한 바뀌지 않는다.

## Kafka Log Cleaner

Kafka는 log을 가지고 log는 parition으로 나누어지고, partition은 segment로 나누어진다. segment는 key,value를 포함하고 있다. Log Cleaner는 log compaction을 수행하고 compaction thread pool을 가진다. 이 thread들은 가장 최신 버전 로그들만 선택해서 segment를 구성한후 이전 segment와 바꾼다. 

## 출처
[http://cloudurable.com/blog/kafka-architecture-log-compaction/index.html](http://cloudurable.com/blog/kafka-architecture-log-compaction/index.html)