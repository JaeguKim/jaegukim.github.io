---
layout: post
title: "Data normalizaton"
date: 2017-07-13
categories: [Database,Theory]
---
## 정의
데이터베이스 내의 애트리뷰트 간의 종속성을 분석해서 하나의 종속성이 하나의 릴레이션으로 표현되도록 분리하는 과정 

## 목적
- 중복된 데이터를 제거
- 삽입,삭제,갱신 이상의 발생을 방지

# Anomaly의 개념 및 종류
- 삽입이상 : 릴레이션에 데이터를 삽입할때 의도와는 상관없이 원하지 않은 값들도 함께 삽입

- 삭제이상 : 릴레이션에서 한 튜플을 삭제할 때 의도와는 상관없는 값들도 함께 삭제되는 연쇄 삭제 현상이 발생

- 갱신이상 : 릴레이션에서 튜플에 있는 속성값을 갱신할 때 일부 튜플의 정보만 갱신되어 정보에 모순이 생기는 현상

## Functional dependency
어떤 테이블 R에 존재하는 필드들의 부분집합을 X와 Y라 할때, X의 한값이 Y에 속한 오직 하나의 값에만 맵핑될 경우 ```Y is functionally dependent on X``` 라고 한다. 이때 X를 determinant(결정자), Y를 dependent(종속자)라 한다.

## Fully-functional dependency
어떤 테이블 R에 존재하는 필드들의 부분집합을 X와 Y라 할때, 
```Y is functionally dependent on X but part of X is not functionally dependent on X then Y is fully functionally dependent on X. ```
Y가 X에 함수적 종속적이면서, X의 일부에는 함수적 종속적이지 않을때, Y는 X에 완전 함수적 종속적이라고 말함.

## 정규화 과정
- 1NF : 모든 도메인이 원자값(atomic value)으로만 구성

- 2NF : 1NF이고, 기본키가 아닌 모든 attribute가 기본키에 대해서 fully functionally dependent

- 3NF : 2NF이고, 기본키가 아닌 모든 attribute가 기본키에 대해 not transitively dependent

- BCNF : 릴레이션 R에서 결정자가 모두 후보키인 관계형
