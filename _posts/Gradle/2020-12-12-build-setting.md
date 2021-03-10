---
layout: post
title: "build setting"
date: 2020-12-12 23:05:00 +0900
categories: [gradle]
---

## api 와 implementation 차이점

- api: 의존 라이브러리 수정시 본 모듈을 의존하고 있는 모듈들 또한 재빌드
A(api) <- B <- C 의 경우 C 에서 A 를 접근할 수 있음
A 수정시 B 와 C 모두 재빌드

- implementaion: 의존 라이브러리 수정시 본 모듈까지만 재빌드
A(implementation) <- B

## compile과 implementation 차이점

| compile | implementaion
| -- | --
| 연결된 모든 모듈의 api가 노출됨. | 직접적으로 연결된 모듈의 api만 노출됨.
| 재컴파일 시간이 오래걸림. | 재컴파일 시간이 짧음.

## 참고 
[https://tjandroid.blogspot.com/2018/11/api-implementation.html](https://tjandroid.blogspot.com/2018/11/api-implementation.html)
