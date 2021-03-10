---
layout: post
title:  "[Docker] docker--compose.yml을 정의하여 Spring boot app 과 MySQL 앱 동시에 실행할때 Connection Link Failure 에러 해결하기"
date:  2020-10-27
categories: [Docker]
---
내가 정의한 커스텀 MySql 이미지와 Spring Boot 서버를 docker-compose를 실행하는데 Connection Link Failure에러가 자꾸 났다.

원인은 의외의 곳에 있었다. 

커스텀 MySql 이미지가 다 실행되기도 전에 Spring Boot 서버가 실행되었기 때문이다.

사실  ```depends_on: - safe-place-db ``` 

구문이 실행되면 실행의 순서가 보장되리라고 생각했는데, 실제로는 safe-place-db가 up 될때까지 보장해주는 것이었다. up이 된 순간 부터는 두가지 컨테이너가 동시에 실행되는 것이다.

따라서 `docker-compose.yml`에  `restart: on-failure:10`  을 추가하여 수정했다.

추가한 구문은 실패할때 10번까지 재실행을 허용하라는 의미이다. 보통 safe-place-db에서 sql 스크립트에대한 실행이 없을때는 depends on 구문으로 충돌이 나는 경우는 없지만 이번 경우는 달랐다.

완성된 `docker-compose.yml` 은 다음과 같다.
``` yml
version: "3"
services:
    safe-place-db:
        container_name: safe-place-db
        image: kimwithglasses/safe-place-db:0.0.1
        ports:
          - 3305:3306        

    safe-place-api:
        container_name: safe-place-api
        image: kimwithglasses/safe-place-api:0.0.1
        restart: on-failure:10
        #build: .
        ports:
          - 80:8080
        depends_on:
          - safe-place-db
```