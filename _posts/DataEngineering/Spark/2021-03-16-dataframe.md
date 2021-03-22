---
layout: post
title: "DataFrame"
date: 2021-03-16 11:35:00 +0900
categories: [DataEngineering,Spark]
---

## DataFrame

![img](https://cdn.app.compendium.com/uploads/user/e7c690e8-6ff9-102a-ac6d-e4aebca50425/f4a5b21d-66fa-4885-92bf-c4e81c06d916/Image/753ace3c801b53535077d9474ecc5f1e/odi_spark_sql_databricks.jpg)

> named column으로 정리된 분산 데이터 컬렉션, 모든 언어에 대한 Unified transformation interface로 transformed 된후 JVM으로 전달된다.

### 내부 구현
- 내부적으로는 RDD와 동일하다.
- row-columnar format으로 저장된다.
- 각각의 파티션에 각각의 컬럼은 min-max 값을 partition pruning을 위해서 저장한다.
- standard RDD보다 압축율이 좋다.

### Optimization, Code Generation

실행이 query optimizer에 의해 최적화된다. DataFrame에 대한 계산이 시작되기전에, Catalyst Optimizer가 DataFrame을 만드는 작업을 실행을 위한 physical plan으로 변환한다. 그리고 operation의 semantic과 데이터 구조를 분석하여, 계산을 빠르게 최적화한다.

high level 관점에서 두가지 종류의 최적화가 존재한다. Catalyst는 predicate pushdown과 같은 logical optimization을 적용한다. optimizer는 filter predicate를 data source에 적용하여 physical execution이 관련없는 데이터는 스킵할 수 있도록 한다. 파케이 파일의 경우에는 전체 블록이 스킵될 수 있고 string 비교는 dictionary encoding을 통해서 더 가벼운 integer 비교 작업으로 변환 될 수 있다. 

두번째로는 Catalyst는 operation을 physical plan으로 변환하고 hand-written code보다 더 최적화된 plan에 대한 JVM bytecode를 생성한다. 예를들면 network traffic을 감소시키기 위해서 broadcast join과 shuffle join사이에 유리한 방향으로 선택한다. 그리고 비싼 객체 할당과 virtual function call을 줄이는 것과 같은 저수준 최적화를 수행한다.

## 출처

[https://databricks.com/blog/2015/02/17/introducing-dataframes-in-spark-for-large-scale-data-science.html](https://databricks.com/blog/2015/02/17/introducing-dataframes-in-spark-for-large-scale-data-science.html)