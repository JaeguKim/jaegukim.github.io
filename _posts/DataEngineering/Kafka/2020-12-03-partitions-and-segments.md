---
layout: post
title: "Topic Configurations"
date: 2020-12-03 19:01:00 +0900
categories: [DataEngineering,Kafka]
---

## Segment

- 토픽들은 파티션으로 구성되 있음

- 파티션들은 segment로 이루어져 있음

- 오직 기록되고 있는 segment만 활성화 되어있음

- 세그먼트는 두개의 index(파일)로 구성됨

    - offset : kafka가 읽어야하는 위치를 찾기위한 인덱스

    - timestamp : timestamp를 가진 메시지들을 찾기 위한 인덱스

    - 카프카는 constant time에 데이터를 찾음.

## Segment Setting

- ```log.segment.bytes``` : single segment의 최대 byte 사이즈(default 1GB)

    - 값이 작아지면 그만큼 partition당 segment수가 많아진다.

    - log compaction이 더 자주 일어난다.

    - 더 많은 파일들을 열고 있어야하므로 error 발생 

- ```log.segment.ms``` : segment를 commit할때 까지 기다리는 시간(segment가 가득 차지 않았을때)

    - default 1 week

    - 값이 작아지면 log compaction이 더 자주 일어난다.


## Log Cleanup Policies

- 많은 Kafka 클러스터들이 데이터를 policy에 따라서 폐기함

- 이 개념을 log cleanup 이라고 부름

- 디스크에 있는 데이터 사이즈 조절, 필요없는 데이터 삭제

- log cleanup은 partition segment에서 일어난다.

- 크키가 작은 segment들이 많으면 log cleanup이 더 자주 발생한다. (더 많은 CPU, RAM 자원을 소모한다.)

- Policy1 : ```log.cleanup.policy=delete``` (모든 유저 토픽에 대해서 default)

    - data의 age에 따라서 삭제(default 1 week)

    - log의 최대 크기에 따라서 삭제(default  -1 == infinite)

- Policy2 : ```log.cleanup.policy=compact``` (__consumer_offsets 토픽에 대한 default)

    - 메시지의 key에 기반하여 삭제

    - active segment 커밋후 중복된 키들을 삭제

    - Segment.ms (default 7 days) : active segment 닫기 까지 기다리는 최대시간

    - Segment.bytes (default 1G) : segement의 최대사이즈

    - Min.compaction.lag.ms (default 0) : message가 compact 되기까지 기다리는 시간

    - Delete.retention.ms (default 24 hours) : compaction으로 데이터가 완전히 삭제되기 전에 삭제된 데이터를 볼수 있는 시간

    - Min.Cleanable.dirty.ratio (default 0.5) : 값이 높을수록 compaction 양이 줄어듬, 더 efficient cleaning, 값이 작을수록 compaction 양은 많아짐, 느린 cleaning

- Policy3 : ```log.retention.hours```

    - data를 보관하는 시간(default 168시간 - 1주)

    - 길수록 디스크 용량을 많이 차지함

    - 짧을수록 데이터 보관량이 줄어듬

- Policy4 : ```log.retention.bytes```

    - 각각의 파티션이 가질수있는 최대 용량(bytes), default -1 - infinite

-  자주 사용되는 조합

    - One week of retention :
    ```log.retention.hours=168```, ```log.retention.bytes``` = -1

    - ```log.retentions.hours=17520, log.retention.bytes = 524288000```

- Policy5 : ```unclean.leader.election```

    - In Sync Replicas(ISR) 이 죽을경우 다음 옵션이 존재함.

        - unclean.leader.election = false : ISR이 online 될때까지 대기 (default)

        - unclean.leader.election = true : non ISR partitions에 데이터를 producing

    - unclean.leader.election = true 일경우 availability는 증가하지만, ISR로 가야하는 데이터는 사라짐

    - 매우 위험한 세팅이므로, 주의해서 세팅해야함.

    - Use case : metrics collection, log collection, data loss가 acceptable한 경우