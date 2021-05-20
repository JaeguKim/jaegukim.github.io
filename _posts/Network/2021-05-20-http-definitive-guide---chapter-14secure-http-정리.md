---
layout: post
title: "[HTTP Definitive Guide - Chapter 14]Secure HTTP 정리"
date: 2021-05-20 19:42:00 +0900
categories: [Network]
---

# Chapter 14 - Secure HTTP

대학생 재학시절 정보보호론 과목에서 배우면서 알던 내용들도 많아서, 모르는 내용 위주로 정리해보았다.

## HTTP vs HTTPS

HTTPS는 HTTP에 transport-level에 security layer(주로 Secure Sockets Layer - SSL, Transport Layer Security - TLS)를 추가함으로써 동작하게 된다. 

## Symmetric Key Cryptography에서 Public Key Cryptography로의 전환 이유

대칭키 방식의 단점은 sender와 receiver가 서로 공유된 키를 가져야 한다는 점이다. 관리해야하는 키의 pair수가 많아진다. 반면 public key 방식은 하나의 public key와 private key만 관리하면 된다. 

## Hybrid Cryptosystems and Session keys

공개키 방식의 문제점은 계산이 느리다는 점이다. 실제로는 대칭키 방식과 공개키 방식을 혼용한다. 예를들면, 공개키 방식을 사용해서 대칭키를 주고 받은후, 대칭키를 가지고 나머지 송수신을 하는 방법을 들수 있다.

## Digital Signature

Digital Signature는 Cryptographic Checksums 이고, 송신자는 원본 메시지를 decoder 함수를 사용해서 값을  생성하고 (이때 개인키가 사용된다.)  수신자는 이 값을 encoder 함수에 통과시켜 원본 메시지와 같은지 비교함으로써 서명을 검증한다. 

이 부분이 직관적이지 않은데, 다음 식을 보면 쉽게 이해할수있다.

> E(D(X)) = X, D(E(X)) = X

여기서 내가 처음든 의문은 나쁜 송신자가 메시지를 변조시키고 그에 대한 digital signature도 자신의 private key로 서명하면 수신자가 이를 어떻게 구분할까라는 질문이었다. 여기서 내가 간과한 부분은 public key와 private key는 서로에게만 호환된다는 점이었다. 송신자가 다른 private key로 서명을 하고, 수신자가 public key로 해당 값을 encoder함수로 복원해보면, 정확한 private key로 서명된 데이터를 제외하고는 원본 메시지와는 다른 값이 나올수 밖에 없다. 즉, 메시지를 변조시킨 경우나, private key를 바꾸고 서명한 경우 모두 수신자 측에서 확인할 수가 있다는 뜻이된다.

## HTTPS 세부 동작

HTTPS에서는 TCP에게 데이터를 보내기전에 SSL or TLS(SSL의 현대판) 계층을 거쳐 데이터를 암호화 한다. 

### HTTPS Schema

- 만약 URL이 http schema이면, 클라이언트는 80번 port를 열고, 데이터를 주고 받는다.
- 만약 https schema라면, 클라이언트는 443번 port를 열고 서버와 handshaking 과정을 거치면서 SSL security parameter들을 주고 받게되며, 이후 암호환된 형태로 데이터를 주고 받게된다.

여기서 http와 https에서 사용하는 포트가 다른 이유는 SSL traffic은 바이너리 프로토콜이기 때문에 일반 80번 port로 보내게 되면 에러로 처리가 될 가능성이 있다. 

### 1. Secure Transport Setup

이 과정에서 클라이언트는 웹서버의 443번 포트를 연다. TCP 연결이 설정되면, 클라이언트와 서버는 SSL 계층을 초기화 하는데, 이때 cryptography 파라미터들과 키들을 주고 받게 된다. handshake 과정이 완료되면 SSL 초기화 과정이 끝나게 되고 클라이언트는 security layer로 메시지를 보낼수 있는 상태가 된다. 이 메시지는 TCP로 보내기지기 전에 암호화 된다.

### 2. SSL Handshake

다음의 일들을 수행한다.

- protocol version number 교환
- cipher(암호 알고리즘) 선택
- identity 확인
- channel을 암호화할 임시 session key 생성

위는 간략한 버전이고 SSL이 사용되는 방법에 따라서 더 복잡해질수도 있다.