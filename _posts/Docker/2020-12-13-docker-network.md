---
layout: post
title: "Docker Network"
date: 2020-12-13 13:39:00 +0900
categories: [Docker]
---

도커내에있는 컨테이너들은 bridge 네트워크에 연결되어있다. 연결된 컨테이너들은 서로 커뮤니케이션 가능하다. 하나의 호스트의 포트번호에는 도커 컨테이너 포트번호는 하나와 매칭된다.

통상적으로 port를 expose할때 ```[container port]:[host port] ``` 로 명시한다.

