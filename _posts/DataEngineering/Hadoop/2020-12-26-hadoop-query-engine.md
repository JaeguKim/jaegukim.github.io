---
layout: post
title: "Hadoop Query Engine"
date: 2020-12-26 23:37:00 +0900
categories: [DataEngineering,Hadoop]
---

## Query Engine

### Apache Drill

- 비관계형 디비(또는 파일스토어)를 위한 SQL쿼리 엔진

    - Hive, MongoDB,HBase

    - flat JSON or HDFS상의 Parquet 파일, S3, Azure, 구글 클라우드, 로컬 파일 시스템

- 구글 Dremel에 기반

- 거의 SQL

### Phoneix

- 트랜젝션을 지원하는 HBase SQL Driver

- 빠르고, low-latency - OLTP 지원

- HBase에 대하여 JDBC connector 노출

- secondary indices, user-defined 함수들 지원

- MapReduce, Spark, Hive, Pig, Flume과 잘 호환

- 장점 

    - HBase에 추가 레이어를 두지 않은것처럼 매우 빠름

    - SQL을 사용할수 있기 때문에 HBase 네이티브 클라이언트를 사용보다 간편하다.

    - 더 복잡한 쿼리들을 최적화하는 작업이 가능하다. 하지만 HBase가 근본적으로 비관계형 데이터베이스라는 사실을 기억해야한다.

### Presto

- Drill과 유사

    - 많은 다른 종류의 big data 데이터 베이스들과 연결가능하고 그 데이터베이스들을 대상으로 쿼리를 실행가능

    - SQL문법과 유사함.

    - OLAP성 작업에 최적화 
    
    - analytical queries, data warehousing

- 페이스북에 의해서 개발되었고 부분적으로 유지되고 있음.

- JDBC, Command-line, Tableau 인터페이스들을 노출시킴.

- 장점

    - Drill과 달리, Cassandra connector지원

    - Facebook, Dropbox, Airbnb에서 사용

    - 단일 프레스토 쿼리로 organization내에 있는 여러 데이터 소스들로부터 데이터들을 콤바인가능

- 연결가능한 데이터베이스들

    - Cassandra

    - Hive

    - MongoDB

    - MySQL

    - Local files

    - Kafka,JMX,PostgreSQL, Redis, Accumulo