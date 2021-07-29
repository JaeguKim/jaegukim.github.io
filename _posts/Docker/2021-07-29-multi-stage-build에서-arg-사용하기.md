---
layout: post
title: "Multi Stage Build에서 ARG 사용하기"
date: 2021-07-29 12:30:00 +0900
categories: [Docker]
---

다음의 Dockerfile이 있다고 가정하자. 

``` dockerfile
#----------- builder -----------#
FROM alpine:3.12.0 AS builder
ARG PROTO_VERSION=3.13.0

# Protobuf
RUN mkdir /protoc \
    && apk add unzip
ADD https://github.com/protocolbuffers/protobuf/releases/download/v$PROTO_VERSION/protoc-$PROTO_VERSION-linux-x86_64.zip /protoc/protoc.zip
RUN unzip /protoc/protoc.zip -d /protoc

# ARG base_img
ARG base_img
FROM $base_img
```

그리고 아래처럼 이미지를 빌드한다고 해보자.

``` sh
docker build -t $(ECR_PATH)/$(ECR_REPO):$(FULL_TAG) . --build-arg base_img=$(SPARK_BASE_IMG)
```

이렇게 할경우 base_img 값에 빈값이 들어가게 되어 빌드에 오류가 발생한다. 

이유는 ARG는 베이스 이미지를 받아오는 FROM 다음 라인부터 값이 지속되지 않는다. 그렇게 때문에 이를 수동으로 renew 해야한다.

즉 아래처럼 도커파일을 수정해야 한다.

``` dockerfile
ARG base_img # 커멘드로 부터 읽력받은 base_img 값 캡처

#----------- builder -----------#
FROM alpine:3.12.0 AS builder
ARG base_img # renew base_img 
ARG PROTO_VERSION=3.13.0

# Protobuf
RUN mkdir /protoc \
    && apk add unzip
ADD https://github.com/protocolbuffers/protobuf/releases/download/v$PROTO_VERSION/protoc-$PROTO_VERSION-linux-x86_64.zip /protoc/protoc.zip
RUN unzip /protoc/protoc.zip -d /protoc

FROM $base_img # 이제 원래 값이 들어가게 된다.
```

## 요약

> Docker의 ARG는 FROM 이전까지만 지속된다. 이를 갱신하기 위해서는 FROM 뒤에 ARG를 한번더 선언해야한다.