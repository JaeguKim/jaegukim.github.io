---
layout: post
title: "Parallel stages with Buildkit"
date: 2022-03-24 12:49:00 +0900
categories: [Docker]
---

## Buildkit 사용

`DOCKER_BUILDKIT=1 docker build -t myapp .` 이렇게 빌드하면 멀티 스테이지 빌드시 서로 독립적인 stage는 병렬로 빌드할 수 있다. [참고](https://blukat.me/2021/07/docker-buildkit-speedup/)
