---
layout: post
title: "five classes of IPv4"
date: 2020-11-09 21:23:00 +0900
use_math: true
categories: [Network]
---
ipv4의 first octet부분을 빨리 알고싶으면 아래그림을 참고하면된다.
![img](/assets/img/post/Network/ipv4-1.png)  
classA의 시작값은 0  
classB의 시작값은 128  
classC의 시작값은 128+64=192  
classD의 시작값은 128+64+32=224  
classE의 시작값은 128+64+32+16=240  
![img](/assets/img/post/Network/ipv4-2.png)  
h = $2^{x}-2$, x : no of zeros  
n = $2^{y}$, y : no of ones

출처 : [Sunny Class](https://www.youtube.com/watch?v=vcArZIAmnYQ&list=PLSNNzog5eydt_plAtt3k_LYuIXrAS4aDZ&ab_channel=SunnyClassroom)