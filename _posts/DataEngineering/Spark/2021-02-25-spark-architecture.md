---
layout: post
title: "Spark Architecture"
date: 2021-02-25 14:56:00 +0900
categories: [DataEngineering,Spark]
---

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

## Application, Job

- Application : SparkContext의 단일 인스턴스이고, 데이터 프로세싱 로직을 저장하고 일련의 Job을 실행

- Job : 데이터 저장, 액션으로 끝나는 일련의 RDD에 대한 transformation

- Stage : 단일 워커에 의해 실행될수 있고 파이프라인 될수 있는 일련의 Transformation.

- Task : 단일 데이터 파티션에 대한 스테이지를 실행. 스케줄링의 기본단위