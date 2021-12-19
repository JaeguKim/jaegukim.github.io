---
layout: post
title: "Kafka Transaction"
date: 2021-12-19 14:19:00 +0900
categories: [DataEngineering,Kafka]
---

## Kafka Transaction

카프카에서 exactly once delievery를 지원하기 위해서 0.11.0.0 이후 버전 이후부터 카프카 트랜잭션 기능을 지원한다. exactly once delievery가 적용되는 범위는 프로듀서부터 컨슈머 까지 연결되는 파이프라인이다. 하지만 컨슈머에서 여전히 중복 데이터 처리가 발생할 수 있다.

## Use case

- 만약 컨슈머가 적재하는 저장소가 unique key를 지원하지 않는 경우 consumer와 producer에 카프카 트랜잭션 적용

- microservice 파이프라인 같이 프로듀서가 중복해서 데이터를 보내는것을 방지하고 싶은 경우

## 출처
[https://blog.voidmainvoid.net/354](https://blog.voidmainvoid.net/3540)

