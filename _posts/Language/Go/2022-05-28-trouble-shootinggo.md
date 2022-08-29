---
layout: post
title: "Trouble Shooting(Go)"
date: 2022-05-28 16:20:00 +0900
categories: [Language,Go]
---

## GoLand No Tests Were Run
test 함수내에 `fmt.printf` 를 사용하는경우, test가 실행되었다고 인식이 되지 않는다.
`fmt.println`을 사용해서 해결가능하다.

## 서버와 gRPC stream으로 통신시 stream으로 부터 데이터를 읽을때 `failed to read frame: read tcp ... use of closed network connection` 에러 메시지 발생
클라이언트에서 서버로 연결시 keepalive param에 충분히 긴 시간으로 설정해서 해결
``` go
	conn, err := grpc.Dial(endpoint, dialOption, grpc.WithKeepaliveParams(keepalive.ClientParameters{
		Time:                300 * time.Second, //5분동안 서버와 연결 유지
		PermitWithoutStream: true,
	}), grpc.WithBlock())
```


