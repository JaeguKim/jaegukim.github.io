---
layout: post
title: "Spark vs MapReduce"
date: 2021-02-25 17:59:00 +0900
categories: [DataEngineering,Spark]
---

## Spark이 MapReduce보다 더 빠른 이유

1. task start up time이 더빠름. Spark은 thread를 복제하고, MR은 새로운 JVM을 생성

2. Faster shuffle. 셔플과정에서 Spark은 데이터를 HDD에 한번만 넣고, MR은 2번 넣는다.

3. Faster workflow. 전형적인 MR workflow는 일련의 MR job이고, 각각의 job은 데이터를 반복할때마다 HDFS에 데이터를 저장한다. Spark은 DAG을 지원하고 파이프라이닝을 지원한다, 중간 결과를 저장할 필요없이 복잡한 workflow를 실행할수 있게한다.(suffle이 필요없다면)

![img](https://i2.wp.com/0x0fff.com/wp-content/uploads/2015/02/SparkRAMProcessing.png?w=400&ssl=1)

4. 캐싱. HDFS도 또한 캐시를 사용할수 있지만, 일반적으로 Spark cache는 꽤 성능이 좋다. 특히 SparkSQL에서 데이터를 최적화된 column oriented form으로 저장하는 경우에서 그렇다.

## 출처
[https://0x0fff.com/spark-misconceptions/](https://0x0fff.com/spark-misconceptions/)