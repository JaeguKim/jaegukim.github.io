---
layout: post
title: "Docker Network"
date: 2020-12-13 13:39:00 +0900
categories: [Docker]
---

- 도커내에있는 컨테이너들은 bridge 네트워크에 연결되어있음.
- 컨테이너들은 서로 커뮤니케이션 가능
- 하나의 호스트의 포트번호에는 도커 컨테이너 포트번호는 하나와 매칭
- 컨테이너들은 inter-communication을 위해서 서로서로의 ip에 의존해서는 안된다.
- custom network를 사용한다면 DNS가 built in 되어있음.