---
layout: post
title: "Flow control, congestion control"
date: 2017-07-17
categories: [Network]
---
# Flow control

- TCP의 수신버퍼의 오버플로우를 방지
- TCP는 상대 TCP에게 rwnd값(수신할 수 있는 data byte용량)을 알려줌
- 각 TCP 연결당 독립적으로 관리

# Congestion Control
- 네트워크의 혼잡을 감지
- 네트워크는 명시적으로 feedback을 제공해주지 않음,종단 TCP가 네트워크 혼잡을 추정
- 혼잡의 징후 : Lost packet(라우터에서 buffer overflow 일어났다고 추정), Long delays(queuing in router buffers)
- cwnd(congestion window size)를 사용하여 transmission rate을 제한 => 연결 하나당 독립적으로 존재, 혼잡이 일어나지 않는 최대 보낼수 있는 크기
