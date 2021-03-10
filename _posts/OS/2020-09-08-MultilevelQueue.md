---
layout: post
title:  "Multilevel Queue (MLQ) Scheduling"
date:   2020-09-08
categories: [OS]
---
# **Multilevel Queue (MLQ) CPU Scheduling이란?**
ready queue에 있는 프로세스들을 스케줄링의 필요성에 따라 여러 종류로 나눠볼수 있다. 예를 들면, foreground(interactive) 프로세스들과 background(batch) 프로세스로 나눠 볼수 있다. 이 두 프로세스들은 다른 스케줄링 요구사항을 갖고있는데, 이것이 Multilevel Queue Scheduling이 사용되는 이유이다.

## **작동방식**
 Ready Queue를 여러 종류의 queue로 나눠보자. 예를들면, system processes, interactive processes, batch processes로 나눠볼수 있다. 이 프로세스 그룹 각각은 자신만의 Queue를 가지고 있다. 아래의 그림을 보자.

![img](/assets/img/post/OS/multilevelQueue1.png)  
각각의 Queue는 각자만의 스케줄링 알고리즘이 있다. 예를들면, queue1과 queue2는 Round Robin 알고리즘을 사용하는 반면, queue3는 FCFS  알고리즘을 사용할수 있다.

큐들 간에는 어떻게 스케줄링 할것인가?

모든 큐들에 프로세스들이 있는 경우를 생각해보자. 어떤 프로세스를 cpu가 선점해야할까? 

이것을 판단하는 방법은 2가지가있다.

## **Fixed priority preemptive scheduling method**
 각각의 queue는 우선순위가 낮은 queue보다 우선순위를 가진다. 예를들어 우선순위 순서가 다음과 같다고 가정해보자 : queue1 > queue2 > queue3. 이 알고리즘에 따르면 batch queue(queue3)는 queue1, queue2가 비어있지 않으면 실행 될수 없다. 만약 batch process(queue 3)가 실행되고 있는데 system(queue1) 또는 interactive process(queue 2)가 ready queue에 들어오면, batch process들은 다른 프로세스들에 의해 선점되게 된다. 

## **Time slicing**
 이 방법으로, 각각의 queue는 CPU time의 일정시간을 할당받게 된다. 예를들면, queue1은 CPU time의 50%정도 차지하고, queue2는 30% 그리고 queue3는 20%정도를 차지 하는경우이다. 

## **예제**
아래의 네가지 프로세스들은 Multilevel queue 스케줄링 알고리즘으로 스케줄링 해보자.

Queue Number는 process의 queue를 나타낸다.

![img](/assets/img/post/OS/multilevelQueue2.png)  
queue1의 우선순위가 queue2보다 높다. queue1은 Round Robin(Time Quantum = 2) 그리고 queue2는 FCFS를 사용한다고 하자.

아래는 문제의 간트차트이다.

![img](/assets/img/post/OS/multilevelQueue3.png)

## **장점과 단점**
- 장점 : 프로세스들이 영구적으로 queue에 할당되므로 스케줄링 오버헤드가 낮다.
- 단점 : 우선순위가 높은 priority queue가 절대 비지 않으면, 몇몇 프로세스들은 기아문제를 겪게된다. 유연하지가 않다.