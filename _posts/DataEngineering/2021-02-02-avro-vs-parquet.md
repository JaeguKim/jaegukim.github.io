---
layout: post
title: "Avro vs Parquet"
date: 2021-02-02 22:35:00 +0900
categories: [DataEngineering]
---

## Apache Avro vs Parquet

**Apache Avro** 는 remote procedure call과 data serialization framework 이고 Apache Hadoop project중 개발되었다. type,protocol을 정의하는데 JSON을 사용하고 compact binary format으로 데이터를 직렬화한다.

- **row based format**이기 때문에, 모든필드들이 접근될필요가 있을때 사용하는것이 좋다.
- 파일들은 block compression을 지원하고 쪼개질수있다.
- streaming data로 쓰여질수있다.(eg. Apache Flink)
- write intensive operation에 적합하다.

**Apache Parquet**, 반면에 Apache Hadoop ecosystem의 open-source column oriented 데이터 스토리지이다. RCFile,ORC와 같은 다른 columnar-storage file format과 유사하다. bulk로 복잡한 데이터를 처리하는 작업에 있어서 효율적인 데이터 압축과 인코딩 스키마를 제공한다.

- **column based format** 이기 때문에, 특정 필드를 접근할 필요가 있을때 사용하는것이 좋다.
- 각각의 데이터 파일은 일련의 row들에 대한 값들을 포함한다.
- 블록들이 처리가 될때까지 기다려야 하므로, streaming data로 쓰여질수 없다. 
- data exploration에 적합하다 - read intensive, complex or analytical querying, low latency data

두가지 포맷이 다음을 지원한다.

- Schema evolution
- Nested dataset