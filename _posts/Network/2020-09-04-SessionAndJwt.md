---
layout: post
title:  "Session VS JWT(Json Web Token)"
date:   2020-09-04
categories: [Network]
---
오늘은 서버와 클라이언트의 인증을 구현하는데 있어서, session과 JWT의 동작방식과 차이점에 대하여 공부해보았다.  
 
# Session 기반 인증
![img](/assets/img/post/Network/sessionBasedAuth.png)  
1. 클라이언트에서 서버로 username, password를 보낸다.

2. 서버는 유저의 로그인정보가 일치하면, session id를 생성하여 메모리에 저장한다.

3. 서버는 클라이언트에게 session id가 담긴 cookie를 전송한다.

4. 클라이언트가 로그인이 되어있는동안, 클라이언트는 서버에 요청할때마다 session id를 함께 전송한다.

5. 서버는 그 session id를 db에 있는 session id와 비교하여 일치하는 경우에 요청에 응답한다.

# JWT 기반 인증
![img](/assets/img/post/Network/jwtBasedAuth.png)   
1. 유저의 로그인정보가 일치하면, 서버는 secret key를 이용하여 JWT를 생성하고 클라이언트에게 전송한다.

2. 클라이언트는 local storage에 JWT를 저장한다.

3. 클라이언트는 모든 요청을 보낼때마다, header에 JWT를 포함시킨다.

4. server는 모든 요청에 대해서 JWT를 검증하고 클라이언트에게 응답한다.

여기서 가장 큰 차이점은 유저의 state가 서버에 저장되지 않는것에 있다. 대부분의 modern web application에서는 JWT를 scalability와 mobile device 인증때문에 사용한다.

# JWT와 Cookie,session의 차이점
다음은 내 나름대로 정리한 표이다.

![img](/assets/img/post/Network/sessionVsJwt.png) 
