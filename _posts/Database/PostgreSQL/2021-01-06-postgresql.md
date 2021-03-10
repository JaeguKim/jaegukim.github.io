---
layout: post
title: "Replica Identity"
date: 2021-01-06 11:02:00 +0900
categories: [Database,PostgreSQL]
---

## Replica Identity

이 세팅에 따라서 업데이트 또는 삭제된 행들을 파악하는데 사용되는 WAL(write-ahead-log)에 기록되는 정보가 달라진다. **logical replication**이 사용중일때를 제외하고는 효력이 없다.

## 4가지 모드

- DEFAULT

    - non system table들에 default 모드

    - pk 칼럼들의 이전값을 WAL에 기록

- USING INDEX

    - named index에 의해 커버된 칼럼들의 이전값만을 기록한다.

    > named index는 unique, not partial, not  deferrable 해야하며 오직 NOT NULL로 마크된 칼럼들만 포함할수 있다.

- FULL

    - 모든 칼럼들의 이전값들을 기록한다.

- NOTHING

    - 이전 row에 대한 아무런 정보도 기록하지 않는다.

