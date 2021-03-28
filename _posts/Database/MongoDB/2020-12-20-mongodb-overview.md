---
layout: post
title: "MongoDB Overview"
date: 2020-12-20 13:07:00 +0900
categories: [Database,MongoDB]
---

## 용어

- Databases

- Collections : rdb에서 행과 같은 개념

- Documents : rdb에서 열과 같은 개념

## Replication Sets

- Single Master구조

- 프라이머리 노드의 데이터 베이스 인스턴스 사본을 백업

    - 세컨더리 노드들은 프라이머리 노드가 다운되면 몇초내에 새로운 프라이머리 노드를 선출가능

    - 프라이머리 노드가 다운됬을때,오퍼레이션 로그가 가용공간을 넘어서는 경우에는 해당 노드를 리커버리하는게 더 어려울 수 있다.
