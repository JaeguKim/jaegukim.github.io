---
layout: post
title: "Elastic Search Overview"
date: 2020-12-16 10:56:00 +0900
categories: [Database,Elasticsearch]
---

## Elasticsearch use case

- 검색엔진 구현

- Application Performance Management(APM) : 어플리케이션 로그, 시스템 통계정보 분석(error, CPU/memeory usage)

- 대용량 데이터 분석

- Anomality Detection

## 특징

- 데이터는 document로 저장됨(relational database의 row와 유사함)

- document는 field로 구성(relational db의 column과 유사)

- REST API로 쿼리를 전달

- Java로 작성됨, Apache Lucene 기반

- scalable, 사용이 간편

## Basic Architecture

- **노드**란 es가 실행되는 인스턴스를 의미

- **노드**들은 데이터들을 저장

- **클러스터**는 여러 노드로구성됨

- 데이터는 JSON object인 document들로 저장됨

- document들은 인덱스로 그룹화됨



