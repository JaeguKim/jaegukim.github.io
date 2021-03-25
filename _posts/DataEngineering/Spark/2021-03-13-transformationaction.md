---
layout: post
title: "Transformation,Action"
date: 2021-03-13 18:30:00 +0900
categories: [DataEngineering,Spark]
---

## Transformation Operation

### 1. Transformation

> RDD를 인풋으로 받아서 한개이상의 RDD를 생산하는 함수

lazy evaluation 이고 action이 실행될때 실행된다. 두가지 기본타입은 map(),filter(),reduceByKey()등의 계산을 적용해서 새로운 RDD를 생산한다.

![img](https://blog.knoldus.com/wp-content/uploads/2019/10/Screenshot-from-2019-09-29-12-07-05.png)

- Narrow transformation - 단일 파티션을 계산하기 위한 데이터는 한개의 parent RDD에서 존재한다. map(),filter()에 의해서 수행된다.

  ![Apache Spark Narrow Transformation Operation](https://d2h0cx97tjks2p.cloudfront.net/blogs/wp-content/uploads/sites/2/2017/08/spark-narrow-transformation-2.jpg)

- Wide transformation - 단일 파티션을 계산하기 위한 데이터는 여러개의 parent RDD에서 존재한다. 대표적으로 groupbyKey()와 reducebyKey가 있다.

![Spark Wide Transformation Operations](https://d2h0cx97tjks2p.cloudfront.net/blogs/wp-content/uploads/sites/2/2017/08/spark-wide-transformation-1.jpg)

### 2. Action

driver program에게 마지막 결과를 리턴하거나 외부 저장소에 데이터를 기록한다.
