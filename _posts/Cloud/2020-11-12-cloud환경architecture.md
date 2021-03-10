---
layout: post
title: "Cloud 환경 Architecture"
date: 2020-11-12 19:44:00 +0900
categories: [Cloud]
---

## 호스트형 가상화 방식
하드웨어 위에 Hypervisor OS를 설치하고 그 위에 가상 서버를 구현하는 방식입니다.

### 장점
한대의 물리서버에 여러 환경에서 동작하는 서버들을 실행할수 있기때문에 자원활용도가 증가

### 단점
여러 서버가 한대의 하드웨어를 공유하므로 서버한대당 사용가능한 자원이 줄어든다. 즉, 성능이 떨어진다.

## Bare Metal 방식
하드웨어 위에 Hypervisor OS설치없이 설치하고 싶은 OS를 직접 하드웨어 위에 설치하는 방식

### 장점
하나의 서버가 하드웨어의 모든 성능을 사용할 수 있음.

### 단점
여러 서버를 가상화방식으로 실행할때보다 하드웨어 자원활용도가 떨어질수 있음.


출처 : [네이버 클라우드 플랫폼 (NAVER Cloud Platform) blog](https://m.blog.naver.com/PostView.nhn?blogId=n_cloudplatform&logNo=221212685823&proxyReferer=https:%2F%2Fwww.google.com%2F)
