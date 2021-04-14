---
layout: post
title: "CrudRepository vs JpaRepository"
date: 2021-04-14 19:41:00 +0900
categories: [Spring]
---

## CrudRepository vs JpaRepository

> 요약 : JpaRepository extends PagingAndSortingRepository which in turn extends CrudRepository

주된 차이점은 아래와 같다.

- [`CrudRepository`](http://static.springsource.org/spring-data/data-commons/docs/current/api/org/springframework/data/repository/CrudRepository.html) : CRUD function들을 제공
- [`PagingAndSortingRepository`](http://static.springsource.org/spring-data/data-commons/docs/current/api/org/springframework/data/repository/PagingAndSortingRepository.html) : pagination과 record sorting하기 위한 방법들을 제공
- [`JpaRepository`](http://static.springsource.org/spring-data/data-jpa/docs/current/api/org/springframework/data/jpa/repository/JpaRepository.html) : provies some JPA-related methods such as flushing persistence context and deleting records in a batch

위에서 언급된 상속관계 때문에, JpaRepository는 CrudRepository와 PagingAndSortingRepository의 기능들을 모두 가진다. 

