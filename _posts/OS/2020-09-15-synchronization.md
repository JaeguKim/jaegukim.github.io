---
layout: post
title:  "Synchronization"
date:   2020-09-15
categories: [OS]
---
# **Synchronization(동기화)**

> 두 프로세스가 같은 공유 데이터와 자원에 접근할 수 있도록, 프로세스들의 실행 순서를 조정하는 일

- 목적 : Race Condition방지, data corruption 방지

- Race condition : 특정 접근 순서에 따라서 실행결과가 달라지는 경우

- silient corruption : data corruption을 운이좋게 피해간 경우

- Nonpreemptive kernel의 경우 race condition은 없지만 평균 대기시간 증가

# **Critical Section**
- process들이 공유변수들을 수정할수 있는 코드의 영역

## **Critical Section Problem**
critical section에는 오직 한 process만 실행되도록 하는 문제

### **해결을 위한 requirement**

- mutual exclusion : critical section에는 오직 한 process만이 실행될수 있다.

- progress 

    - 자기의 임계 영역에서 실행중인 프로세스가 없고 자신의 임계영역으로 진입하려고 하는 프로세스들이 있다면, 나머지 영역(Critical Section or Leave Section)에서 실행 중이지 않은 프로세스들만 임계 영역으로 진입할 프로세스를 결정하는 데 참여할 수 있으며, 이 선택은 무기한 연기될 수 없다.

- Bounded Waiting : 어떤 process가 임계영역에 들어가기 위해 대기하는 시간은 유한해야한다.

    - 프로세스가 자신의 임계 영역에 진입하려는 요청을 한 후부터 그 요청이 허용될 때까지 다른 프로세스들이 자신의 임계영역에 진입하도록 허용되는 횟수는 한계 또는 제한이 있어야 한다.

### **구현방법**

- Strict Alternation : 아래와 같은 방식이다.

    For Process Pi
    ``` 
    Non - CS   
    while (turn ! = i);   
    Critical Section   
    turn = j;   
    Non - CS  
    ```

    For Process Pj
    ```
    Non - CS   
    while (turn ! = j);  
    Critical Section   
    turn = i ;  
    Non - CS   
    ```

    - progress requirement를 만족하지 않음. 한 프로세스가 실행되고나서 다른 process가 실행되기 전까지는 무기한 연기됨. 

- Peterson’s algorithm : progress, Bounded waiting 모두 만족

    - 단점 : Busy waiting, empty while loop를 돌리면서 CPU 리소스를 잡아먹게된다.

- Special H/W instruction : atomic operation을 코드로 구현하는 것이 아니라, 하나의 instruction으로 구현.

    - 단점 : 하드웨어 설계자들이 멀티 프로세서 환경에서 원자적으로 instruction을 구현하는 것은 간단하지 않다.

- Mutex Locks : critical section 문제를 해결하기 위한 SW tool, 하지만 busy waiting이 발생하는 문제점이 있다.
    bush waiting이란 instruction을 수행하면서 기다리는 현상을 말한다.(CPU cycle 낭비)

### **Busy Wating의 해결책** : 

1) process를 semaphore의 waiting queue에 넣고 wait state로 전환

2) CPU schedular가 다른 process를 schedule

3) 다른 process가 signal 함수를 호출하면 ready queue로 이동 

### [자세한 보충설명 link](https://stackoverflow.com/questions/33143779/what-is-progress-and-bounded-waiting-in-critical-section)
