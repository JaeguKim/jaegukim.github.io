---
layout: post
title: "Cache,Persist"
date: 2021-02-23 14:19:00 +0900
categories: [DataEngineering,Spark]
---

## Spark DataFrame Cache, Persist

Spark Cache,Persist는 잡의 퍼포먼스를 개선하기위해 반복적이고 상호작용이 많은 spark 어플리케이션에 대해서 DataFrame/Dataset을 최적화 하는 기술이다. 

```cache()``` 와 ```persist()``` 함수를 사용하여, spark은 데이터 프레임 중간 결과를 저장하는 최적화 메커니즘을 제공하여, 연속적인 액션들이 재사용될수 있도록 한다.

데이터 셋을 persist할때, 각 노드는 partition된 데이터를 메모리에 저장하고 그 데이터셋에 대해서 다른 action연산을 할때 데이터를 재사용한다. 노드의 persist된 데이터는 fault-tolerant하다. 즉, 어느 한 데이터 셋 파티션이 손실되더라도, 자동으로 그것을 생성한 원래 transformation을 사용하여 다시 계산된다.



### DataFrame Caching,Persistence의 이점

- Cost efficient - spark 연산은 매우 비싼 작업이고 따라서 계산결과를 재사용하여 비용을 절감할수있다.
- Time efficient - 반복되는 계산결과를 재사용하는것은 시간을 절약할수 있다.
- Execution time - job의 실행시간이 절약되므로 더 많은 잡을 같은 클러스터에 실행할수 있다.



### Spark Cache Syntax 과 예시

```cache()``` 함수는 DataFrame 또는 DataSet을  디폴트로 storage level이 ```MEMORY_AND_DISK``` 로 저장한다.

``` cache() : Dataset.this.type ``` 

Spark ```cache()``` 함수는 내부적으로 ```persist()``` 를 호출하고 내부적으로 DataFrame 이나 Dataset의 결과를 캐시하기위해 ```sparkSession.sharedState.cacheManager.cacheQuery``` 를 사용한다.

**예시**

``` scala
val spark:SparkSession = SparkSession.builder()
    .master("local[1]")
    .appName("SparkByExamples.com")
    .getOrCreate()

  //read csv with options
  val df = spark.read.options(Map("inferSchema"->"true","delimiter"->",","header"->"true"))
    .csv("src/main/resources/zipcodes.csv")
  
  val df2 = df.where(col("State") === "PR").cache()
  df2.show(false)

  println(df2.count())

  val df3 = df2.where(col("Zipcode") === 704)

  println(df2.count())
```



### DataFrame Persist Syntax와 예시

persist함수는 다음의 storage level을 설정가능하다. ```MEMORY_ONLY```. ```MEMORY_AND_DISK```,```MEMORY_AND_DIST_SER```, ```DIST_ONLY```, ```MEMORY_ONLY_2```, ```MEMORY_AND_DISK_2``` 등

**문법**

```scala
persist() : Dataset.this.type
persist(newLevel : org.apache.spark.storage.StorageLevel) : Dataset.this.type)
```



첫번째 시그니처는 디폴트로 ```MEMORY_AND_DISK```로 저장한다. 두번째는 storage level을 인자로 받는다.

**예시**

``` scala
val dfPersist = df.persist()
val dfPersist = df.persist(StorageLevel.MEMORY_ONLY)
```



### Unpersist syntax 

Spark은 persist된 데이터가 사용되지 않으면  LRU 알고리즘에 따라서 자동으로 삭제한다. 수동으로 데이터를 삭제하는것도 가능하다. ```unpersist()``` 함수는 dataset에 대한 모든 블럭들을 메모리와 디스크에서 삭제한다.

**문법**

```scala
unpersist() : Dataset.this.type
unpersist(blocking : scala.Boolean) : Dataset.this.type
```



### Spark Persist storage level

- ```MEMORY_ONLY``` - RDD ```cache()``` 함수의 기본값이고 RDD나 DataFrame을 역직열화 포맷으로 JVM에 저장. 메모리가 충분하지 않으면 몇몇 파티션은 저장이 안되고 필요할때 다시 계산된다. RDD의 경우와 달리 ```MEMORY_AND_DISK``` 레벨보다는 느리다. 느린이유는 저장되지 않은 파티션들을 다시 계산하고 인메모리 칼럼 표현으로 계산하는 과정이 비싸기 때문이다.
- ```MEMORY_ONLY_SER``` - ```MEMORY_ONLY``` 와 동일하지만 차이점은 RDD를 직렬화 포맷으로 저장한다는 차이가 있다. MEMORY_ONLY 보다는 더 적은 공간을 소모하지만 역직렬화를 하기 위해서 CPU cycle이 필요하다.
- ```MEMORY_ONLY_2``` - ```MEMORY_ONLY``` 와 동일하지만 각 파티션을 두개의 클러스터 노드로 복제한다.
- ```MEMORY_ONLY_SER_2``` - ```MEMORY_ONLY_SER``` 와 동일하지만 각 파티션을 두개의 클러스터 노드로 복제
- ```MEMORY_AND_DISK``` - DataFrame or Dataset의 기본 행동이다. JVM상에 역직열화된 객체들이 저장된다. 요구 공간이 현재 이용가능한 공간을 초과하면, 일부 파티션들이 디스크로 저장되고 필요시 디스크에서 읽힌다. I/O 과정때문에 속도가 떨어질수있다.
- ```MEMORY_AND_DISK_SER```
- ```MEMORY_AND_DISK_2```
- ```MEMORY_AND_DISK_SER_2```
- ```DISK_ONLY```
- ```DISK_ONLY_2```

## 출처
[https://sparkbyexamples.com/spark/spark-dataframe-cache-and-persist-explained/](https://sparkbyexamples.com/spark/spark-dataframe-cache-and-persist-explained/)