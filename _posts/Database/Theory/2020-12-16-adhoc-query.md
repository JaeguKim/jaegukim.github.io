---
layout: post
title: "Adhoc Query"
date: 2020-12-16 23:27:00 +0900
categories: [Database,Theory]
---

Adhoc쿼리란 코드가 실행될때마다 변경되는 쿼리를 말한다.

다음의 코드 예를 보자.

``` javascript
var newSqlQuery = "SELECT * FROM table WHERE id = " + myId;
```

위 코드를 보면 ```myId```의 값에 따라서 쿼리문이 변경됨을 알수있다.

ad hoc query의 반대로는 Stored Procedure같은 predefined query가 있다.