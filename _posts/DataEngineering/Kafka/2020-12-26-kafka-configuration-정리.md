---
layout: post
title: "Kafka configuration 정리"
date: 2020-12-26 17:06:00 +0900
categories: [DataEngineering,Kafka]
---

| config | 설명
| -- | --
| auto.offset.reset | **latest** : 가장 마지막 offset부터, **earliest** : 가장 처음 offset부터, **none** : 해당 consumer group이 가져가고자 하는 topic의 consumer offset정보가 없으면 exception 발생시킴
| max.poll.records | 단일 호출 poll()에 대해 최대 레코드 수를 조정. `max.partition.fetch.bytes`에 지정된 byte크기에 제약을 받는다.
| delete.retention.ms | log compacted topic을 위해서, tombstone 마커를 제거 마커를 얻기까지 걸리는 시간
| retention.ms | "delete" retention policy를 사용할 경우, 예전 log segment를 버리기전에 log를 얻을수 있는 최대시간.  컨슈머가 데이터를 얼마나 빨리 읽어야하는지를 나타냄. -1로 설정될경우 time limit이 존재하지 않고, 디폴드 값은 7일(604800000)이다.
| max.partition.fetch.bytes | maximum number of bytes the server will return per partition. default is 1MB
| default.replication.factor | default replication factors for automatically created topics
| min.insync.replicas | When a producer sets acks to "all" (or "-1"), this configuration specifies the minimum number of replicas that must acknowledge a write for the write to be considered successful.
| Preferred Leader Election | partition leader인 broker가 fail될 경우, 다시 broker가 정상화되었을때 해당 broker가 partition leader로 선택된다. 만약 leader가 죽어있는 상황에서 다른 in-sync replicas또한 online이 아니라면 해당 partition은 unavailable 상태가 된다. consistency를 HA보다 우선시 한것으로 볼수 있다.
| Unclean Leader Election | partition leader인 broker가 fail될 경우, out-of-sync replicas를 가진 broker가 leader가 될수 있다. 이 경우 원래 leader였던 broker가 다시 살아나도 다시 리더로 설정하지 않는다. HA를 consistency보다 우선한다고 볼수 있다.

