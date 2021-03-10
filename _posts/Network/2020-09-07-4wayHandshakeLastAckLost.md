---
layout: post
title:  "4-way-handshake에서 마지막 ACK 가 유실된다면?"
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

만약 B to A로 가는 마지막 FIN이 유실된다면 어떤 일이 발생할까? B는 ACK를 받지 않았으므로 ACK를 받을때까지 FIN을 재전송 할것이다. A가 결국 FIN을 받게되면 TIME_WAIT상태에 돌입한다.

> A -----FIN-----> B  
> FIN_WAIT_1       CLOSE_WAIT  
> A <----ACK------ B  
> FIN_WAIT_2  
>  
> (B can send more data here, this is > half-close state)  
>  
> A  X<--FIN------ B  
> FIN_WAIT_2       LAST_ACK  
> (timeout waiting for ACK)  
> A <----FIN------ B    
> TIME_WAIT  
> A -----ACK-----> B  
> |                CLOSED  
> 2MSL Timer  
> |  
> CLOSED  

여기서 마지막 ACK가 유실된다면? B는 A가 FIN을 받지 않았다고 생각할것이고 FIN을 재전송할 것이다. 즉, B의 관점에서 보면 A가 FIN이 유실되었을 때와 같다. 하지만 A관점에서보면 다른데, A는 TIME_WAIT상태 or CLOSED 상태에 있기 때문이다. A가 TIME_WAIT 시점에서 B로부터 FIN을 받게되면 A는 ACK를 재전송할것이다.

아래그림은 TIME_WAIT 상태에서 B로부터 FIN이 날라온 경우이다.

> A -----FIN-----> B  
> FIN_WAIT_1       CLOSE_WAIT  
> A <----ACK------ B  
> FIN_WAIT_2  
>
> (B can send more data here, this is > half-close state)  
> 
> A <----FIN------ B  
> TIME_WAIT        LAST_ACK  
> A -----ACK-->X   B  
> TIME_WAIT        LAST_ACK  
>                 (timeout waiting for > ACK)  
> A <----FIN------ B  
> A -----ACK-----> B  
> |                CLOSED  
> 2MSL Timer  
> |  
> CLOSED  

만약 A가 CLOSED 상태에 있으면, RESET을 전송할것이다. 

둘중에 어떤 상황이 됐건, B는 연결을 종료할수 있게된다.

아래그림은 CLOSED 상태에서 B로부터 FIN이 날아온 경우이다.

> A -----FIN-----> B  
> FIN_WAIT_1       CLOSE_WAIT  
> A <----ACK------ B  
> FIN_WAIT_2  
>   
> (B can send more data here, this is > half-close state)  
> 
> A <----FIN------ B  
> TIME_WAIT        LAST_ACK  
> A -----ACK-->X   B  
> TIME_WAIT        LAST_ACK  
> |  
> 2MSL Timer  
> |  
> CLOSED  
>                 (timeout waiting for > ACK)  
> A <----FIN------ B  
> A -----RST-----> B  
>                  CLOSED  