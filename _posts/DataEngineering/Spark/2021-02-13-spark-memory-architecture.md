---
layout: post
title: "Spark Memory Architecture"
date: 2021-02-13 17:44:00 +0900
categories: [DataEngineering,Spark]
---

## Spark Legacy Memory Architecture 

### Executor

**worker node** 에서 수행되는 Spark application의 JVM process이다. 여러 스레드로 task들을 수행하며 관련있는 데이터 파티션들을 유지한다.



### Executor Memory 구조

![img](https://i0.wp.com/0x0fff.com/wp-content/uploads/2015/03/Spark-Heap-Usage.png?w=475&ssl=1)

YARN에 10gb의 executor을 워커노드상에서 요청할때, 10gb 전체가 이용가능하다고 생각하기 쉽지만 사실 **safety** 리전이 존재한다. 이는 OOM을 방지 하기 위한 공간이다. **safety** 공간은 10%점유하고 configuration에는 ```spark.storage.safetyFraction``` 이라고 명시된다. 

> 결국, 10gb executor는 9gb의 사용가능한 공간이 있다.

#### Storage

```spark.storage.memoryFraction``` 와 ```spark.shuffle.memoryFraction```. 그리고 각각 60%, 20% 로 설정되어있다. 따라서 10gb의 executor에서, **storage** 공간은 ``` 10 gb * 90% * 60% ``` , 즉 5.4gb 이다.

이는 executor는 caching data를 제외하고 5.4 gb를 소유하고 있음을 의미한다. 만약 데이터가 메모리에 들어가지 않는다면, **storage level** 에 따라서 disk에 남은 데이터가 저장되거나 가능한 만큼만 캐싱한다. 

#### Shuffle

다른 config로는 ```spark.shuffle.safetyFraction``` 이 있는데, 디폴트값은 80%이다(JVM heap 전체의 80%). **shuffle** 영역은 pre-reduce aggregation에 사용된다. 이 영역이 사용되는 한가지 예는 ```reduceByKey``` 작업을 할때인데, reduce작업이 로컬에서 먼저 수행되고 **shuffle memory**가 결과를 저장하기 위해 사용된다. ```reduceByKey``` 결과가 이 영역에 들어가지 않으면, spark은 disk에 결과를 저장한다. 지금 예시에서는 ```80% * 20% ``` 또는 executor당 1.6gb 가 할당된다.

#### Unroll

unroll process에 할당된 RAM의 양은 ```spark.storage.unrollFraction * spark.storage.memoryFraction * spark.storage.safetyFraction = 0.2 * 0.6 * 0.9 = 0.108 or 10.8% ``` 이다. 이 메모리영역은 데이터를 메모리로 unrolling 할때 사용된다. unroll이 필요한 이유는 무엇일까? spark은 데이터를 serialized, deserialized form으로 저장가능하다. serialized 데이터는 직접적으로 사용될수 없고 사용하기전에 unrolling 작업을 해야한다. 따라서 이 메모리 영역은 unrolling에 사용되는 메모리 영역이다. storage RAM과 공유되고, 이말은 데이터를 unroll 하기위해서 메모리가 필요할때 이 작업이 Spark LRU cache에 저장되어있는 일부 파티션 정보가 지워질수 있음을 의미한다.



### Caching

Executor 수를 결정하기전에, caching에 대해서 살펴보자. ```.persist``` 또는 ```.cache``` 가 호출될때, 데이터가 메모리에 캐싱된다. ```rdd.cache()``` 는 ```rdd.persist(storageLevel.MEMORY_ONLY)``` 와 동일하다. 몇가지 storage level이 존재하는데, rdd가 메모리에 들어가지 않을때 수행할 정책을 결정한다. 

- **MEMORY_ONLY** :  java Object로 데이터를 저장한다. int나 string에 대한 java object에는 추가로 저장할 데이터가 필요하므로 공간 효율적이지는 않지만, 가장 빠른방법이다. 데이터가 메모리에 완전히 캐싱될수 있다면 사용하면된다.
- **MEMORY_ONLY_SER** : 데이터를 serialized format으로 저장한다. 메모리에 더많은 데이터를 저장할수 있지만 사용될때 serialize/deserialize를 해야하므로 CPU의 부하가 조금 증가할수 있다. 
- **MEMORY_AND_DISK_SER** : 데이터를 serialized format으로 저장한다. 메모리에 들어가지 않는 데이터는 disk에 serialized format으로 저장된다. 만약 캐싱이전에 heavy processing, join/reduce 작업이 있다면 좋은 선택이될수 있다.

## Spark New Memory Architeture

Spark 1.6.0 부터, 메모리 관리모델이 변경되었다. 이전 메모리 모델은 ```StaticMemoryManager``` 클래스에의해 구현되었고 이제는 legacy라 불린다. 호환성을 위해서 legacy 모델을 활성화 시킬수 있다. ```spark.memory.useLegacyMode``` 파라미터를 활성시키면 되는데, 디폴트로는 꺼져있다.

새로운 메모리 관리 모델은 ```UnifieldMemoryManager```로 구현이 된다.

![img](https://i0.wp.com/0x0fff.com/wp-content/uploads/2016/01/Spark-Memory-Management-1.6.0.png?w=1261&ssl=1)

1. **Reserved Memory** : 이 메모리는 시스템에 의해서 예약된다, 사이즈는 하드코딩 되어있다. spark 1.6.0에서는 300MB이고 이는 spark 메모리 리전 계산에서 고려대상이 아니다. 참고로 Reserved Memory의 1.5배 이상의 힙공간을 executor에게 제공하지 않으면 에러가 발생한다.

2. **User Memory** : **Spark Memory** 할당한후 남은 공간이다. RDD transformation에서 사용될 자료구조를 저장할수 있다. ``` User Memory Space = (“Java Heap” – “Reserved Memory”) * (1.0 – spark.memory.fraction) = (“Java Heap” – 300MB) * 0.25. ```  만약 할당받은 공간이상을 사용하면 OOM error가 발생한다.

3. **Spark Memory** : Apache Spark에 의해 관리되는 메모리 풀이다. ```Spark Memory Space = (“Java Heap” – “Reserved Memory”) * spark.memory.fraction = (“Java Heap” – 300MB) * 0.75.``` 이 공간은 **Storage Memory**와 **Execution Memory**로 나누어진다. 이 둘의 경계는 ```spark.memory.storageFraction``` 파라미터로 설정된는데 디폴트 값은 0.5이다. 이 경계는 스태틱하지 않고 메모리 부족시 경계가 옮겨질수 있다.

   1. **Storage Memory**. 이 공간은 cached data, 일시적으로 serialized data가 저장되는 unroll에 의해서 사용된다. 또한 모든 brodcast 변수들또한 cached block에 저장된다. 모든 brodcast 변수들은 캐시에 저장되는데, **MEMORY_AND_DISK** persistence 수준으로 저장된다. 여기 저장된 데이터는 HDD로 evict 될수 있다.
   2. **Execution Memory**. 이 공간은 Spark task를 실행하는 동안 요구되는 객체들을 저장하는데 사용된다. 예를들어 shuffle intermediate buffer를 저장하는데 사용될수 있다. 또한 hash aggregation step을 위해서 hash table을 저장하는데 사용될수 있다. 충분한 메모리가 없다면 디스크로 데이터를 저장하는 기능도 수행한다. 하지만 이 공간에 있는 블락들은 다른 thread(task)에 의해서 강제로 evict될수 없다.

   **Execution Memory** 가  **Storage Memory** 를 빌릴수 있는 몇가지 경우가 있다.

   - Storage Memory 풀에서 공간이 남아있을때. 이 경우 storage memory 사이즈를 감소시키고 Execution memory 사이즈를 증가시킨다.
   - Storage Memory 공간크기가 초기 Storage Memory 설정공간을 초과하고 이 공간이 전부 사용되고 있을때. 이 경우 Storage Memory 크기가 초기 사이즈가 될때까지 데이터를 evict할수 있다.

   반대로 **Storage Memory** 또한 **Execution Memory** 공간을 빌릴수 있다. 이때 **Execution Memory**에 빈공간이 반드시 존재해야 한다.

   만약 Spark cache를 사용한다면, executor에 캐싱된 데이터의 전체 용량은 최소 초기 Storage Memory 리젼 크기만큼 될것이다. 우리는 storage region 크기가 최소 초기 크기만큼은 된다는 것을 보장할 수 있다. 그 이유는 초기 크기보다 더 작아지도록 하면서, 데이터를 evict 할수는 없기 때문이다. 그러나 만약 Execution Memory가 이미 초기 사이즈를 넘어섰고, 그후에 storage memory에 데이터를 채워넣었다면, Execution memory에 있는 데이터를 강제로 evict할수는 없게된다, 따라서 실행하는 동안 storage memory 리젼은 초기 사이즈보다 더 적은 크기를 가질 수 밖에 없다.


## 출처

[http://0x0fff.com/spark-architecture/](http://0x0fff.com/spark-architecture/)

[http://0x0fff.com/spark-memory-management/](http://0x0fff.com/spark-memory-management/)