---
layout: post
title: "Kafka configuration 정리"
date: 2020-12-26 17:06:00 +0900
categories: [DataEngineering,Kafka]
---

| config | 설명
| -- | --
| auto.offset.reset | **latest** : 가장 마지막 offset부터, **earliest** : 가장 처음 offset부터, **none** : 해당 consumer group이 가져가고자 하는 topic의 consumer offset정보가 없으면 exception 발생시킴
| max.poll.records | 단일 호출 poll()에 대해 최대 레코드 수를 조정.
| delete.retention.ms | log compacted topic을 위해서, tombstone 마커를 제거 마커를 얻기까지 걸리는 시간
| retention.ms | "delete" retention policy를 사용할 경우, 예전 log segment를 버리기전에 log를 얻을수 있는 최대시간.  컨슈머가 데이터를 얼마나 빨리 읽어야하는지를 나타냄. -1로 설정될경우 time limit이 존재하지 않고, 디폴드 값은 7일(604800000)이다.

