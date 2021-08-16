---
layout: post
title: "Init Containers"
date: 2021-08-16 23:40:00 +0900
categories: [Kubernetes]
---

## Init Containers

Pod은 여러 컨테이너를 가지고 있는데, 하나이상의 init container를 가질수 있다. init container는 app container가 시작되기전에 실행된다.

- Init containers always run to completion.
- Each init container must complete successfully before the next one starts.