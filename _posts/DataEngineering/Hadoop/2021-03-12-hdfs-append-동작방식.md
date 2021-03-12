---
layout: post
title: "HDFS append 동작방식"
date: 2021-03-12 20:54:00 +0900
categories: [DataEngineering,Hadoop]
---

## HDFS append 동작방식

1. HDFS는 마지막 블럭에 append한다. 그리고 만약 블럭이 가득차면 새로운 블럭을 생성한다.
2. 오직 하나의 write or append만이 특정 시점에 허용된다. 다른 인스턴스가 write or append하려면 파일을 닫아야한다.
3. 마지막 블럭이 복제되지 않으면, append는 실패한다. append는 single replica에 기록이되고, replicas에게 복제된다.

## 출처

[https://issues.apache.org/jira/browse/HDFS-265](https://issues.apache.org/jira/browse/HDFS-265)