---
layout: post
title: "[Trouble Shooting] cannot resolve column(numeric column name) in Spark Dataframe"
date: 2021-02-10 09:59:00 +0900
categories: [DataEngineering,Spark]
---

다음과 같은 스키마가 있다고 하자.

```
scala> data.printSchema
root
 |-- 1.0: string (nullable = true)
 |-- 2.0: string (nullable = true)
 |-- 3.0: string (nullable = true)
```

이 경우 다음 라인을 실행하면 에러가 난다.

```
scala> data.select("2.0").show
```

Exception:

> org.apache.spark.sql.AnalysisException: cannot resolve '`2.0`' > given input columns: [1.0, 2.0, 3.0];;

## 해결방법

``` scala
data.select("`2.0`").show
```

dot은 struct type내에 있는 칼럼을 접근하기 위해 예약되어있기때문에, backtick으로 dot을 escaping해야한다.

## 출처
[https://stackoverflow.com/questions/42698322/cannot-resolve-column-numeric-column-name-in-spark-dataframe/42698362#42698362](https://stackoverflow.com/questions/42698322/cannot-resolve-column-numeric-column-name-in-spark-dataframe/42698362#42698362)