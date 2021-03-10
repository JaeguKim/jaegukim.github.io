---
layout: post
title: "HTTPS Handshake with TLS"
date: 2020-11-16 17:55:00 +0900
categories: [Network]
---

# HTTPS Handshake with TLS 1.2
`https://` 프로토콜 prefix로 HTTP 리퀘스트를 보내면, 먼저 TCP connection이 3-way handshake를 사용해서 설정된다. 아래의 파란선이 연결수립과정이다.

> HTTPS 프로토콜의 기본 포트번호는 443이다.

![TLS 1.2 Handshake](https://upload.wikimedia.org/wikipedia/commons/d/d3/Full_TLS_1.2_Handshake.svg)

[출처](https://commons.wikimedia.org/wiki/File:Full_TLS_1.2_Handshake.svg)

TCP 커넥션이 일어나고, TLS handshake이 일어난다. 
## 1. client가 **TLS 1.2 protocol layer**로 감싼뒤에 빈 패킷을 보낸다.
- 이 layer는 metadata와 **Client Hello** 메세지를 포함한다.
- 보낼때 다음정보도 함께 보낸다.
cipher suites 리스트, hostname을 지칭하는 server name indication(SNI)
- SNI정보는 서버가 hostname과 일치하는 SSL certificate을 리턴하는데 사용된다.

## 2. 서버가 **Client Hello** packet을 받고나서는 빈 패킷으로 답장한다.
- 클라이언트가 제공한 선택지중 서버가 선택한 cipher suite 정보를 패킷에 추가한다.
- 클라이언트가 SNI value를 사용해서 요청한 domain name에 해당하는 SSL certicate를 패킷에 추가한다.
- 그리고 **Server Hello Done** 메시지를 보낸다.

## 3. 클라이언트가 SSL certificate를 수신하고 검증한다. 
- certificate는 서버가 선택한 **cipher suite**의 **public key**를 포함한다.
**ciphter suite**는 또한 **cryptographic algorithms**과 **hash function**을 포함하는데 이들은 data를 암호화하고 검증하는데 사용된다.

간단한 cipher suite의 예로는 아래와 같다.

>TLS_**RSA**_WITH_**AES**_256_CBC_**SHA**

만약 서버가 위의 cipher suite를 선택했다면, 서버가 공유 비밀키를 암호화하기 위해서 RSA 알고리즘을 선택했다는 의미이다.
클라이언트와 서버에 의해서 사용되는 암호화 알고리즘은 **AES 256bit**이다.

cipher suite의 마지막부분은 **digital signature**를 만들기 위한 one-way hashing 함수이다.

## 4. 클라이언트와 서버가 cipher suite에 동의하면, 커뮤니케이션이 시작된다. 
- 클라이언트는 데이터 암호화를 위한 shared secret key를 생성한다. 위에서 명시한대로 **AES 대칭키 알고리즘**에 대한 **256bit**크기의 key를 생성한다. 

## 5. SSL certificate로부터 얻어진 서버의 **RSA 공개키**를 사용하여 클라이언트는 공유 키를 암호화하여 서버에 전송한다. 
- 이때 메시지는 **Client Key Exchange**로 세팅한다.
- 패킷은 또한 **Change Cipher Spec**메시지를 포함하는데, 이는 클라이언트가 **합의된 cipher spec**을 사용하고 있다는 의미이다.

## 6. 서버가 이 패킷을 받으면, private key를 사용하여 data를 복호화한후, 대칭키를 구한다. 
- 아무도 이 private key를 모르므로 **shared secret key는 아무도 읽을수 없다.**
- **Change Cipher Spec** 메시지를 보고 서버는 read/write 모드를 cipher spec으로 변경한다. 그리고 **shared secret key**를 사용해서 **handshake message**를 복호화한다.

## 7. handshake message가 **Finished**이므로, 클라이언트에게 **Changed Cipher Spec** 메시지와 **Finished**를 보낸다.
- 이는 서버가 합의된 cipher spec을 사용함을 의미한다.
- **Finished** 메시지를 공유키로 암호화하여 보낸다.

## 9. 클라이언트가 패킷을 받으면 **TLS 1.2 handshake가 완료된다** 

이제 application data가 TCP 채널을 통하여 암호화/복호화 과정을 거칠수 있게된다.

[출처](https://medium.com/jspoint/a-brief-overview-of-the-tcp-ip-model-ssl-tls-https-protocols-and-ssl-certificates-d5a6269fe29e)