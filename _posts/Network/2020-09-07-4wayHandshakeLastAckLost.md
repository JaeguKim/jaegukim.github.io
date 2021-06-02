---
layout: post
title:  "4-way-handshake에서 마지막 ack가 필요한 이유"
date:   2020-09-07
categories: [Network]
---
이글은 stack exchange에 올라온

[Why is the last ACK needed in TCP four way termination](https://networkengineering.stackexchange.com/questions/38805/why-is-the-last-ack-needed-in-tcp-four-way-termination) 질문에 대한 번역입니다.

> A -----FIN-----> B  
> FIN_WAIT_1       CLOSE_WAIT  
> A <----ACK------ B  
> FIN_WAIT_2
>
>(B can send more data here, this is >half-close state)
>
> A <----FIN------ B  
> TIME_WAIT        LAST_ACK  
> A -----ACK-----> B  
> |                CLOSED  
> 2MSL Timer
> |  
> CLOSED  
위는 4-way-handshake을 요약한 그림이다.

왜 마지막 ACK가 필요한가? 만약 마지막 ACK가 없다고 가정해보자. 먼저 두가지 상황이 생길수 있다.

- 첫번째 상황은 B에서 A로 가는 FIN이 도착한 경우이다. 이 경우에는 A 입장에서는 TIME_WAIT 상태에 돌입후 2MSL 시간후에 연결이 좋료 된다. 하지만 B는 ACK를 전달받지 못해서 무기한 대기한다. 

- 두번째 상황은 B에서 A로 가는 FIN이 유실된경우이다. 이 경우에는 A 입장에서는 TIME_WAIT 상태에 돌입할 수 없으므로, FIN_WAIT_2 상황에서 무기한 대기한다. 

마지막 ACK가 존재한다면 첫번째, 두번째 상황에서 해결이 가능하다. B는 ACK를 전달받을 수 있고, A는 TIME_WAIT에 도달할때까지 FIN(A->B)을 재전송해서, 결국은 FIN(B->A)를 수신할 수 있기 때문이다.