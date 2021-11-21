---
layout: post
title: "Trouble Shooting(Docker)"
date: 2021-11-21 16:29:00 +0900
categories: [Docker]
---

## COPY 커멘드시 wildcard 사용
`COPY src/* dest/` : src내에 있는 subdirectory 구조를 고려하지 않고, 파일들을 dest 경로로 복사
`COPY src/ dest/` : subdirectory 구조를 고려하여 복사