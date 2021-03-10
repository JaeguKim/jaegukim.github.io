---
layout: post
title:  "4-way handshake는 왜 4단계를 거쳐야하는가?"
date:   2020-09-07
categories: [Network]
---
다음은 stackoverflow에 올라온 [질문](https://stackoverflow.com/questions/46212623/why-tcp-connect-termination-need-4-way-handshake)에대한 번역글입니다.

connection이 setup 되는 과정은 다음과 같다.  

(3-way-handshake)

Client ——SYN—–> Server

Client <—ACK/SYN—- Server —-①

Client ——ACK—–> Server

connection이 terminate 되는 과정은 다음과 같다.

(4-way-handshake)

Client ——FIN—–> Server

Client <—–ACK—— Server —-②

Client <—–FIN—— Server —-③

Client ——ACK—–> Server

이때 왜 ②과 ③이  ①과 같이 하나로 묶을수 없는가?

four-way handshake는 two-way handsakes가 두개있는것으로 볼수있다.

Client ------FIN-----> Server

Client <-----ACK------ Server
지금 이시점에 클라이언트는 FIN_WAIT_2 상태에 있고 서버로부터 FIN 패킷을 기다리고 있다.

TCP는 전이중 통신(Full Duplex: 두 대의 단말기가 데이터를 송수신하기 위해 동시에 각각 독립된 회선을 사용하는 통신 방식이다.) 이기 때문에 클라이언트측에서 보내는 방향의 연결이 끊어져서 데이터를 더이상 보낼수 없다고 해도, 클라이언트는 여전히 다른쪽 방향으로 데이터를 받는것은 가능하다. 따라서 클라이언트는 서버에서 클라이언트로 향하는 half-duplex가 종료될때까지 기다려야한다.

서버에서 FIN을 client에게 보내면, 클라이언트는 ACK를 서버에게 보내고 TIME_WAIT 상태에 들어가게된다.

> 결론 : ②과 ③은 합쳐질수 없다. 왜냐하면  ②과 ③은 다른상태에 속하기 때문이다. 서버가 클라이언트로 
> 부터 FIN을 받았을때, 서버에서 더이상 보낼데이터가 전혀없다면 ②과 ③이 합쳐질수있다.