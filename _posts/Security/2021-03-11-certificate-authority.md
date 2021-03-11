---
layout: post
title: "Certificate Authority"
date: 2021-03-11 14:46:00 +0900
categories: [Security]
---

## SSL certificates

세가지 안전한 커뮤니케이션을 위한 원칙 존재한다.

- Data Encryption
- Data Integrity
- Data Authenticity : 의도하고 있는 대상과 커뮤니케이션 하고 있는가

SSL은 Data Authenticity를 고려하기 위해 존재한다.

SSL certificate은 Certificate Authority(CA)라 불리는 기관에 의해서 private key를 사용하여 서명된 binary이다.

브라우저가 신뢰하는 certificate은 두가지 타입이있다.

- Root CA : GlobalSign, ...
- Intermediate CA

```google.com``` 서버는 SSL certificate을 보내는데 다음과 같이 생겼다.

![Image for post](https://miro.medium.com/max/484/1*PoKM30FYwcLemZHQl8XPSg.png)

issuer 정보를 보면, Google Trust Services에 의해서 서명되었음을 확인할수 있다. 또한 public key 정보를 확인할수 있다. Google Trust Service의 SSL certificate이 이미 설치되었기 때문에,  ```google.com``` 에서 보낸 SSL certificate에 있는 digital signature를 검증할수 있다. 만약 man-in-the-middle이 잘못된 SSL certificate을 보낸다면 브라우저는 인증된 CA로 부터 서명되지 않았다고 판단할것이다.

Google Trust Services는 intermediate CAL이다. 다수의 웹사이트와 많은 예산을 갖고있는 기관들은 매일 CA에게 인증서 사인을 요청하는 대신에, 중간 CA가 되어서 GlobalSign과 같은 root CA에게 certificate를 만들어달라고 요청을 보낸다.  certificate의 private key를 사용해서 다른 SSL 인증서에게도 사인을 할수있다. 브라우저가 해야하는 것은 CA의 부모 CA를 검사해서 digital signature를 검증하는 것이다.

root CA까지 타고 올라가서, 브라우저는 chain of trust를 만들수 있다. 위 스크린샷을 보면 GlobalSign이 root CA이고 GTS CA의 부모 CA임을 확인할수 있다. 어느 중간 certificate가 실패하면, 전체 trust chain이 실패로 처리되고 웹 사이트는 데이터를 정송하고 접근하기 위험한 상태가 된다. 브라우저는 신뢰되고 안전한 연결을 나타내기 위해서 아래와 같이 green padlock을 보여준다.

![Image for post](https://miro.medium.com/max/600/0*r-N-rbzpFQVrat-6.png)

## 출처

[https://medium.com/jspoint/a-brief-overview-of-the-tcp-ip-model-ssl-tls-https-protocols-and-ssl-certificates-d5a6269fe29e](https://medium.com/jspoint/a-brief-overview-of-the-tcp-ip-model-ssl-tls-https-protocols-and-ssl-certificates-d5a6269fe29e)