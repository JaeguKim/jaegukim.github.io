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

왜 마지막 ACK가 필요한가? 

B가 A에게 FIN을 보낼때의 의미는 B가 더이상 보낼 데이터가 없음을 A에게 알려주기 위함이다. 만약 FIN이 유실된다면 A는 B가 아직 보낼 데이터가 있다고 인식하게 되고 계속 대기하게 된다. 그렇게 때문에 B입장에서는 A가 FIN을 확실히 받았는지를 알아야 한다. 그렇게 하기 위해서, A는 마지막 ACK를 응답으로 보내야만 한다.