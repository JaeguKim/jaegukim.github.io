---
layout: post
title: "Fernet Key"
date: 2021-12-08 21:45:00 +0900
categories: [DataEngineering,Airflow]
---

## Fernet

Fernet은 대칭키 인증 cryptography 구현체이다. Airflow는 커넥션과 변수의 configuration에 있는 패스워드들을 암호화하기 위해 Fernet을 사용한다.