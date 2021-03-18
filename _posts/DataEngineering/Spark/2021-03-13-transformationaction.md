---
layout: post
title: "Transformation,Action"
date: 2021-03-13 18:30:00 +0900
categories: [DataEngineering,Spark]
---

## Transformation Operation

### 1. Transformation

dataset을 함수에 전달하고 새로운 dataset을 리턴하는 작업

lazy evaluation 이고 action이 실행될때 실행된다. 두가지 기본타입은 map(),filter()이다.

- Narrow transformation - 하나의 파티션에서 일부만이 결과로 반환된다.

  ![Apache Spark Narrow Transformation Operation](https://d2h0cx97tjks2p.cloudfront.net/blogs/wp-content/uploads/sites/2/2017/08/spark-narrow-transformation-2.jpg)

- Wide transformation - 하나의 파티션에 있는 데이터가 여러 파티션에 보내질수있다. 대표적으로 groupbyKey()와 reducebyKey가 있다.

![Spark Wide Transformation Operations](https://d2h0cx97tjks2p.cloudfront.net/blogs/wp-content/uploads/sites/2/2017/08/spark-wide-transformation-1.jpg)

### 2. Action

driver program에게 마지막 결과를 리턴하거나 외부 저장소에 데이터를 기록한다.
