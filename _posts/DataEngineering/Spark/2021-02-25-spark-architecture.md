---
layout: post
title: "Spark Architecture"
date: 2021-02-25 14:56:00 +0900
categories: [DataEngineering,Spark]
---

# Spark의 동작방식

![img](https://d2h0cx97tjks2p.cloudfront.net/blogs/wp-content/uploads/sites/2/2017/08/Internals-of-job-execution-in-spark.jpg)

1. spark-submit을 사용해서, application을 제출한다.
2. spark-submit이 명시된 jar의 main() 함수를 실행하고, driver를 실행한다.
3. driver는 sparkContext를 생성하고, cluster manager(eg. MESOS, YARN)에게 자원을 요청한다.
4. cluster manager가 driver를 대신해서 executor를 실행한다.
5. driver는 task를 executor에게 보낸다.
6. executor는 task를 실행하고 결과를 cluster manager를 통해서 driver에게 보낸다.

# Spark 용어

## SparkContext
Spark RDD, accumulator, broadcast variable을 생성하고 Spark job을 실행한다. 주로 다음 일을 한다.
- spark application의 현재 상태 얻기
- job을 취소하기
- Stage 취소하기
- job을 비동기/동기로 실행하기

## SparkShell
command line 환경 제공

## Job
action에 의해서 생성되는 일련의 RDD에 대한 transformation. job은 여러 stage로 구성된다. 

## Stage
단일 워커에 의해 실행될수 있고 파이프라인 될수 있는 일련의 Transformation. 여러 task로 구성된다.

## Task
spark에 의해서 수행되는 작업의 단위로 executor JVM에서 하나의 스레드로 동작한다. 하나의 task에 하나의 partition이 맵핑된다.

## Partition

데이터를 읽기위한 대부분의 메소드에서 RDD에대한 partition수를 명시할수 있다. HDFS에서 파일을 읽을때는 Hadoop InputFormat을 사용한다. 디폴트로는 InputFormat에 의해서 리턴된 각각의 input split은 RDD에 있는 하나의 partition으로 맵핑된다. HDFS상의 대부분의 파일에서 input split은 HDFS위에서 저장된 단일 데이터 블록당 하나로 대응된다. 데이터 블록 사이즈는 대략 64MB 또는 128MB 정도이다. 대략적으로 HDFS상의 데이터는 정확히 블록 단위로 나누어지고 처리될때 record splits 나누어진다.  text file에서는 splitting character는 newline char이지만 sequence file에서는 block end이다. 압축파일에서는 예외가 있는데 - 전체 텍스트 파일이 압축되있다면 전체파일이 하나의 input split, partition이 되므로 수동으로 repartition 해야한다.

여기서 단일 partition 데이터를 처리하기위해서, spark은 하나의 task를 생성한다, task는 데이터와 가까이 위치한 task slot에서(Hadoop block location, Spark cached paritition location) 실행된다.

## Spark Application
SparkContext의 단일 인스턴스이고, 데이터 프로세싱 로직을 저장하고 일련의 Job을 실행

## Driver

- Spark Shell(Scala, Python, R)에 대한 entry point

- SparkContext가 생성되는 곳

- RDD를 execution graph로 변환

- graph를 여러 stage로 나눔

- task를 스케줄하고 실행을 통제

- RDD와 파티션에 대한 메타데이터 저장


## Executor

![img](https://i2.wp.com/0x0fff.com/wp-content/uploads/2015/03/Spark-Architecture-On-YARN.png)

- JVM heap or HDD에 데이터 저장

- 외부 저장소로부터 데이터 읽어들임

- 외부 저장소에 데이터를 씀

- 데이터 프로세싱 수행





