---
layout: post
title: "MapReduce"
date: 2020-12-15 13:44:00 +0900
categories: [DataEngineering,Hadoop]
---

## MapReduce

![img](https://github.com/JaeguKim/Cookbook/raw/master/images/MapReduce-Process-Detailed.jpg)

데이터를 두가지 단계로 처리한다 : map phase, reduce phase.
map phase에는 HDFS로 부터 데이터를 읽는다. 각각의 dataset은  input record라고 부른다.
reduce phase에는 실제 계산이 수행되고 결과가 저장된다. 그리고 저장 타깃은 database,HDFS 등이 될수 있습니다.
mapper와 reducer들은 클러스터에서 병렬적으로 실행된다.

### 동작방식
map phase 도중, key-value pair를 생성하여 reducer에 전달하고, reducer에서 key로 소팅된다. 즉, reduce phase에 대한 input record는 같은 key를 가진 mapper의 값들이다.
그리고 reduce phase는 해당 key와 value를 가지고 연산을 하고 결과를 저장한다.
얼마나 많은 mapper와 reducer를 사용할수 있을까? parallel map과 reduce process의 갯수는 클러스터에 가용한 CPU core 수에 달려있다. 모든 mapper와 reducer는 한 코어를 사용한다.

### Node에 작업 할당 방식

1. Cient Node에서 작업을 시작함

2. YARN(어떤 잡이 어느 클러스터, 어느 호스트에서 실행되고 있는지 알고있음)이 어느 클러스터, 어느 호스트가 작업수행이 가능한지 알아냄.

3. Client node는 YARN의 Resource Manager에게 맵리듀스 잡을 의뢰함. 그 동안 Client Node는 HDFS에 작업에 필요한 데이터를 복사함.

4. NodeManager위에서 MapReduce Application Master가 동작함. NodeManager는 다른 MapReduce Task들을 감시함. Resource Manager와 함께 MapReduce노드들에게 어떻게 데이터를 분배할것인지 정함.

5. 각각의 MapReduce노드들은 HDFS와 커뮤니케이션 하면서 데이터를 읽고 씀.

- (추가) Resource Manager는 MapReduce 노드에게 테스크를 할당할때 되도록이면 필요한 데이터를 가지고 있는 HDFS 호스트에서 MapReduce 테스크를 실행하도록 한다. 만약, 그것이 불가능하면 네트워크상 최대한 가까운 위치에있는 HDFS 노드에 있는 데이터를 가지고 Task를 수행하도록한다.

- (추가) 하나의 머신에서 여러개의 MapReduce Task가 동작할수도 있다.

### 오류 대응방식

- Application Master는 worker task의 에러나 지연현상들을 모니터링한다.
    - 필요하면 task를 재시작
    - 다른 노드에 task를 할당

- Application Master가 죽는다면?
    - YARN이 Application Master를 재시작하려고 시도

- 클러스터에 있는 머신들(Application Master도 포함)이 모두 죽는다면?
    - Resource Manager가 재시작하려고 시도

- Resource Manager도 죽는다면?
    - Zookeeper를 사용하여 백업 Resource Manager를 띄울수있다.

### MapReduce의 한계점

![img](https://github.com/JaeguKim/Cookbook/raw/master/images/MapReduce-Process.jpg)

MapReduce의 문제점은 여러 map, reduce 프로세스를 연결하는 방법이 간단하지 않다는 것이다. 각각의 reduce process가 끝나면 데이터는 어딘가 저장되어야한다. 이는 복잡한 analytics process를 수행하는것이 힘들다는 것을 의미한다.

두번째 문제점은 streaming analytics를 수행하는것이 어렵다는것이다. 잡이 실행되기까지 시간이 소요되고, 기본 몇분을 기다리는것이 정상이다.

## 출처 
[https://github.com/JaeguKim/Cookbook/blob/master/sections/03-AdvancedSkills.md#How-does-mapreduce-work](https://github.com/JaeguKim/Cookbook/blob/master/sections/03-AdvancedSkills.md#How-does-mapreduce-work)