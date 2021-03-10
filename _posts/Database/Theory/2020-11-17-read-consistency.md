---
layout: post
title: "Read Consistency"
date: 2020-11-17 22:39:00 +0900
categories: [Database,Theory]
---

# Read Consistency

## Transaction-level read consistency (트랜젝션 수준 읽기 일관성)

- 트랜젝션의 각 SQL문의 질의는 그 트랜젝션 시작전에 커밋한 데이터만을 본다.

- **물론 해당 트랜젝션이 변경한 데이터는 볼수있다.**

## Statement-level read consistency(statement 수준 읽기 일관성)

- 트랜젝션의 각 SQL문의 질의는 그 statement 시작전에 commit한 data만을 본다.

- **물론 해당 트랜젝션이 변경한 데이터는 볼수있다.**