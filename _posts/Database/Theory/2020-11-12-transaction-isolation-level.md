---
layout: post
title: "Transaction Isolation Level"
date: 2020-11-12 20:05:00 +0900
categories: [Database,Theory]
---
## 트랜잭션 고립 수준 (Transaction Isolation Level)
- 트랜잭션들끼리 일관성있는 데이터를 얼마나 허용할 것인지 정해놓은 수준
- 즉, 트랜잭션 수행 중 다른 트랜잭션이 해당 데이터를 조회하는 것이 가능한지의 정도를 결정해 놓은 것
- 고립 수준이 높을 수록 일관성은 보장되지만 그만큼 동시성이 떨어진다. (성능 하락)

| 고립 수준  | 설명  |
|---|---|
| Read Uncommited (Level 0)  | - 트랜잭션 수행 중이거나 아직 commit 되지 않은 데이터를 다른 트랜잭션에서 Read 하는 것을 허용<br>- Dirty Read, Non Repeatable Read, Phantom Read 발생 가능  |
| Read Commited (Level 1)  | - 트랜잭션 수행이 완료되고 commit 된 데이터만 다른 트랜잭션에서 Read하도록 허용<br>- Non Repeatable Read, Phantom Read 발생 가능<br>- 일반적으로 DBMS에서 Default로 설정하는 레벨  |
| Repeatable Read (Level 2)  | - 특정 트랜잭션에서 읽고 있는 데이터는 다른 트랜잭션에서 수정/삭제 (Update/Delete)가 불가능하다.<br> - 삽입(Insert)은 가능하다.<br>- Phantom Read 발생 가능   |
| Serializable (Level 3)| - <br>- 모든 이상 현상 방지 가능<br>- 하지만 그만큼 동시성이 떨어져서 성능이 하락함 |

## 이상 현상 종류

| 이상 현상  | 설명  |
|---|---|
| Dirty Read  | - 어떤 트랜잭션에서 아직 실행이 끝나지 않은 트랜잭션에 의한 변경사항을 보게 되는 경우 |
| Non Repeatable Read  | - 어떤 트랜잭션이 같은 쿼리를 2번 실행하는데 그 사이에 다른 트랜잭션이 수정/삭제를 하는 경우 |
| Phantom Read  | - 어떤 트랜잭션이 같은 쿼리를 2번 실행하는데 그 사이에 없던 레코드가 추가된 경우 |

## [추가 설명](https://nesoy.github.io/articles/2019-05/Database-Transaction-isolation)
