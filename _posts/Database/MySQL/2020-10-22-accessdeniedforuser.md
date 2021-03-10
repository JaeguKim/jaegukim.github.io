---
layout: post
title: "[DB Trouble Shooting] java.sql.SQLException - Access denied for user 예외"
date: 2020-10-22 +0900
categories: [Database,MySQL]
---
아래와 같이 선언해서는 위의 에러가 계속 발생한다.
``` sql
grant all privileges on moBack to 'springstudent';
```
다음과 같이 선언하면 에러가 해결된다.
``` sql
grant all privileges on moBack.* to 'springstudent'@'%';
```