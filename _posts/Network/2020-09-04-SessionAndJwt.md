---
layout: post
title:  "Session VS JWT(Json Web Token)"
date:   2020-09-04
categories: [Network]

---

오늘은 서버와 클라이언트의 인증을 구현하는데 있어서, session과 JWT의 동작방식과 차이점에 대하여 공부해보았다.  

## Session 기반 인증

![img](https://miro.medium.com/max/842/1*Hg1gUTXN5E3Nrku0jWCRow.png)

1. 클라이언트에서 서버로 username, password를 보낸다.

2. 서버는 유저의 로그인정보가 일치하면, session id를 생성하여 메모리에 저장한다.

3. 서버는 클라이언트에게 session id가 담긴 cookie를 전송한다.

4. 클라이언트가 로그인이 되어있는동안, 클라이언트는 서버에 요청할때마다 session id를 함께 전송한다.

5. 서버는 그 session id를 db에 있는 session id와 비교하여 일치하는 경우에 요청에 응답한다.

### 단점

> 리소스 요청이 있을때마다, 세션 저장소에 매번 조회를 해야한다.

## JWT 기반 인증

![img](https://miro.medium.com/max/842/1*PDry-Wb8JRquwnikIbJOJQ.png)

1. 유저의 로그인정보가 일치하면, 서버는 secret key를 이용하여 JWT를 생성하고 클라이언트에게 전송한다.

2. 클라이언트는 local storage에 JWT를 저장한다.

3. 클라이언트는 모든 요청을 보낼때마다, header에 JWT를 포함시킨다.

4. server는 모든 요청에 대해서 JWT를 검증하고 클라이언트에게 응답한다.

여기서 가장 큰 차이점은 유저의 state가 서버에 저장되지 않는것에 있다. 대부분의 modern web application에서는 JWT를 scalability와 mobile device 인증때문에 사용한다. 

### 한계점

> 1. Secret값이 탈취가 될 경우, JWT token을 생성 및 복호화 할 수 있다.
> 2. token 자체를 누군가 탈취한다면, 해당 token으로 인증을 성공시킬 수 있게된다.
> 3. 이를 대비해서, token의 유효기간을 짧게 두는 방법이 있는데, 이 경우 로그인을 자주 해야하는 문제가 생기고 이를 해결하기 위해 나온것이 refresh token이다. refresh token을 보냄으로써 서버에게 새로운 token을 발급받아서 로그인을 연장하는 방법이다. 하지만 refresh token또한 탈취가 될 수 있기때문에, refresh token 정보 또한 유효기간을 두어야 한다. 이를 구현하기 위해서 Redis와 같은 휘발성 DB에 저장하여 구현할 수 있다. 이 경우 server는 refresh token의 유효성을 검사하는 로직도 처리해야 하는 단점이 생긴다.

