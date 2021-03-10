---
layout: post
title:  "CPU Scheduling Algorithm"
date:   2020-09-15
categories: [OS]
---
# **CPU Scheduling Algorithm**

## **Non Preemptyive Scheduling**

### FCFS(First Come First Served)
- 도착한 순서에 따라 차례로 CPU를 할당하는 기법

### SJF(Shortest Job First) 
- 실행 시간이 가장 짧은 프로세스에게 먼저 CPU를 할당하는 기법

## **Preemptive Scheduling**

### **Priority Scheduling**

- 가장 높은 우선순위를 가진 process를 schedule

- SJF는 Priority Scheduling의 special case

- FCFS는 equal priority를 가진 priority scheduling

- 문제점 : 낮은우선순위 Process들이 Schedule 될수 없는 경우 발생(Starvation)

- 해결책 : Aging => 점진적으로 process들의 우선순위를 증가시킴

### **Round Robin Scheduling**

- queue에 있는 프로세스를 주어진 time quantum만큼 실행

- 실행이 끝나지 않으면 queue에 enqueue

- time quantum이 너무크면 FCFS이고, time quantum이 너무 작으면 context switching하는데 overhead가 증가함

### **Multilevel Queue Scheduling**

- 하나의 ready queue를 여러 독립 큐로 나누고, 각각의 queue에 독자적 스케줄링 알고리즘 사용

- process들은 하나의 queue에 영구적으로 할당됨

- 상위 queue가 비어야 하위 queue들이 실행가능

### **Multilevel Feedback Queue Scheduling**

- process들이 queue들 사이로 이동 가능
- 특정 그룹의 준비상태 큐에 들어간 프로세스가 다른 준비상태 큐로 이동할 수 있음
- 각 준비상태 큐마다 시간 할당량을 부여하여 그 시간 동안 완료하지 못한 프로세스는 다음 단계의 준비상태 큐로 이동됨.