---
layout: post
title: "gRPC vs REST"
date: 2022-08-09 13:36:00 +0900
categories: [Web]
---

## gRPC vs REST

- REST

  - 장점
    - additional technology 필요없음
  - 단점
    - url path와 http method의 조합으로 디자인하는데 상당한 노력이 필요

- gRPC

  - 장점

    - 좀더 심플하고 직접적인 방법으로 remote procedure 정의가능
    - code generator를 사용해서 REST 보다 쉽게 구현가능
    - HTTP/2의 효율적인 connection management 사용, binary payload로 효율적 전송가능

  - 단점

    - 클라이언트와 서버에 special software가 필요하고 gRPC generated code가 빌드 프로세스에 포함되어야 함.

    