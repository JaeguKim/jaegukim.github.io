---
title: "[DB Trouble Shooting]public key retrieval is not allowed"
layout: post
date: 2020-10-22 +0900
categories: [Database,MySQL]
---
- mysql 8.x 버전 이후로 발생

- jdbc url에 allowPublicKeyRetrieval=true&useSSL=false 필요

- 예시:
```
jdbc:mysql://localhost:3306/dev-product?useUnicode=true&characterEncoding=utf8&allowPublicKeyRetrieval=true&useSSL=false
```
[출처](https://joont92.github.io/java/java-mysql-%EC%97%B0%EB%8F%99%EC%8B%9C-%EC%98%A4%EB%A5%98/)
