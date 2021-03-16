---
layout: post
title: "Multilevel Feedback Queue Scheduling(MLFQ)"
date: 2020-11-10 17:53:00 +0900
categories: [OS]
---
이번글은 [링크](https://www.geeksforgeeks.org/multilevel-feedback-queue-scheduling-mlfq-cpu-scheduling/)에 있는 글을 번역한 글입니다.

이 스케줄링은 Multilevel Queue(MLQ)와 흡사하지만 프로세스가 큐들사이를 이동할수 있습니다. 
MLFQ는 프로세스들의 행동(실행시간)을 분석하여 우선순위를 바꿉니다.  
![img](/assets/img/post/OS/mlfq.png)

위그림에서 queue1과 queue2가 round robin (각각 time quantum 4,8) 으로 스케줄링 되고 queue3는 FCFS로 스케줄링 된다고 가정합니다.  
MFQS의 한가지 구현방법은 아래와 같습니다.

1. 처음 들어오는 프로세스들은 queue1으로 들어갑니다. 

2. queue1에서 프로세스들이 4unit내에 실행이 완료된다면, 이 프로세스의 우선순위는 바뀌지 않고, 다음에 ready queue에 프로세스가 들어오면 다시 queue1에서 실행을 시작합니다.

3. queue1에있는 프로세스가 4unit내에 실행되지 않으면, 우선순위가 감소하게 되고 queue2로 이동하게 됩니다.

4. queue2에서도 위의 2,3단계를 똑같이 반복하지만 이번에는 time quantum이 8입니다. 이번에는 8unit만에 실행이 되지 않으면 더 낮은 우선순위 큐로 이동합니다.

5. 마지막 큐에서, 프로세스들은 FCFS 방식으로 스케줄링됩니다.

6. 낮은 우선순위 큐에있는 프로세스는 더 높은 우선순위의 큐들이 비어있어야 실행됩니다.

7. 낮은 우선순위 큐에있는 프로세스는 더 높은 우선순위의 큐들로 할당된 프로세스에 의해서 인터럽트 됩니다.

**위의 구현의 문제점** - 낮은 우선순위큐에있는 프로세스는 CPU time이 짧은 프로세스들때문에 Starvation에 빠질수있습니다.   

**해결책** - 일정 시간후에 프로세스들의 우선순위를 최우선으로 높여줍니다.

**이러한 복잡한 스케줄링이 필요한 이유**
- multilevel queue scheduling보다 더 유연하다

- turnaround time을 최적화 시켜주는 SJF와 같은 알고리즘을 써야하는데, 프로세스별 실행시간은 미리 알려져있지 않다. MFQS는 time quantum만큼 실행하고 우선순위를 변경할수 있다.(만약 실행시간이 긴 프로세스라면) 따라서 process의 과거 행동에 기반하여 미래를 예측한다. 따라서 더 짧은 실행시간을 가진 프로세스를 먼저 실행하고려고 노력하고 따라서 turnaround time을 최적화할수 있다.

- 응답시간을 줄여준다.

# 예시
burst time이 40초인 프로세스가 있다고 가정하자. MLFQ 스케줄링 알고리즘이 사용되고, queue의 time quantum은 2초이고 각각의 level에서 5초만큼 증가한다고 가정하자. 프로세스가 interrupt되는 횟수와 실행을 종료하는 queue는?

# 해답
Process P는 총 40초의 실행시간이 필요하다.
1. Queue1에서 2초간 실행되고 interrupt되고 queue2로 이동  
2. Queue2에서 7초간 실행되고 interrupt되고 queue3로 이동
3. Queue3에서 12초간 실행되고 interrupt되고 queue4로 이동
4. Queue4에서 17초간 실행되고 interrupt되고
queue5로 이동
5. Queue5에서 2초간 실행되고 실행이 완료됨
따라서 process는 4번실행되고 queue5에서 실행이 완료된다.

# MLFQ 스케줄링의 장단점
## 장점:
1. 프로세스들이 queue들사이를 이동하도록 허용하므로 유연하다.
2. 너무 오래 기다리고 있는 프로세스들을 낮은 우선순위 큐에서 높은 우선순위 큐로 이동시킨다.

## 단점:
1. CPU overhead가 커진다.
2. 복잡하다.

