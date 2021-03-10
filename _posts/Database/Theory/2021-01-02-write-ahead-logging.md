---
layout: post
title: "Write-ahead logging"
date: 2021-01-02 11:02:00 +0900
categories: [Database,Theory]
---

## Write-ahead logging

컴퓨터과학에서 **write-ahead logging(WAL)** 은 데이터베이스 시스템에서 atomicity와 durability를 제공하기위한 기술중 하나이다. 변경정보가 로그로 먼저 기록되고, **Stable Storage**에 반드시 기록되어야하고 그리고 데이터베이스에 기록된다.

> Stable Storage란 write연산에 대한 원자성을 보장하는 데이터 스토리지 기술의 분류이다.

WAL을 사용하는 시스템에서는, 모든 수정사항들은 log로 쓰여진다음에 적용되다. 보통 redo와 undo정보는 로그에 저장된다.

예를들어보면, 어떤 연산을 수행하던 프로그램이 있었는데 갑자기 컴퓨터에 파워가 꺼졌다고 가정하자. 재시작이 되면 프로그램은 작업이 성공했는지, 부분적으로 성공했는지, 아니면 실패했는지를 알필요가 있을것이다. 만약 WAL이 사용된다면, 프로그램은 로그 파일을 검사해서 정상적인 프로그램 수행결과와 비교할수 있다. 이 비교결과를 바탕으로 프로그램은 이전 수행했던 작업을 취고하거나 유지시킬수 있다.

WAL은 데이터 베이스의 업데이트가 [in-place](https://en.wikipedia.org/wiki/In-place_algorithm) 하게 수행될수 있도록 허락한다. atomic  updates를 구현하는 다른 방법은 shadow paging이며, 이 방법은 in-place하지 않다. In-place 업데이트를 하는것의 장점은 인덱스들과 블럭리스트들을 수정할 필요성을 감소시키는 것에 있다.



## 출처

[https://en.wikipedia.org/wiki/Write-ahead_logging](https://en.wikipedia.org/wiki/Write-ahead_logging)

