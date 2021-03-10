---
layout: post
title: "Process vs Thread"
date: 2021-03-04 13:10:00 +0900
categories: [OS]
---

## Process vs Thread

### Process

PCB는 어느 프로세스의 동작을 통제함. PID, Process Priority, Process State 등을 포함한다. 다른 프로세스와 메모리를 공유하지 않는다.

### Thread

프로세스의 일부이고 3가지 상태를 가질수 있다 : running,ready,blocked. Thread는 프로세스에 비해서 종료시간이 짧다. 여러 스레드들은 데이터,코드,파일 등의 정보를 공유한다. 세가지 방법으로 스레드를 구현할수 있다.

1. Kernel-level thread
2. User-level thread
3. Hybrid thread

![img](https://media.geeksforgeeks.org/wp-content/uploads/20190522155604/Untitled-Diagram-361.png)



### Process의 특징

- 생성시 독립적인 시스템 콜을 호출해야함
- 데이터와 정보를 공유하지 않는다.
- IPC(Inter-Process Communication) 메커니즘을 사용하여 서로 소통하고, 시스템콜의 호출 횟수가 많다.
- 프로세스는 독립적인 stack,heap,data 영역을 가지고 있다.

### Thread의 특징

- 하나의 시스템 콜로 여러 스레드를 생성가능하다.
- 스레드는 데이터 영역을 공유한다.
- 스레드는 인스트럭션,글로벌,힙 영역을 공유한다. 하지만 독립적인 register와 stack영역을 가지고 있다.
- 커뮤니케이션 비용이 낮다.(시스템콜 호출이 필요없다.)



### 차이점

| Parameter | Process | Thread
| -- | -- | --
|정의| 실행중인 프로그램 | 프로세스의 segment
|Termination/Create Time/Context Switching Time| 길다 | 짧다


