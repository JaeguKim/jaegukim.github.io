---
layout: post
title: "Flink Architecture"
date: 2022-03-10 14:14:00 +0900
categories: [DataEngineering,Flink]
---

## Flink Architecture

![The processes involved in executing a Flink dataflow](https://nightlies.apache.org/flink/flink-docs-release-1.14/fig/processes.svg)

### JobManager

세개의 컴포넌트로 구성되어있다.

- ResourceManager

  - Flink cluster에 리소스 할당과 해제, 리소스 스케줄링의 단위인 task slot관리

- Dispatcher

  - Flink app submit을 위한 REST Interface 제공
  - Job execution정보를 제공하는 WebUI 제공

- JobMaster

  - 단일 JobGraph 실행을 관리, 각각의 Job은 JobMaster를 가지며 Flink cluster에서 동시에 실행될 수 있다.

  JobManager는 HA를 위해서 여러개가 떠있기도 한다.



### TaskManager

Task slot으로 구성되며 각각의Task slot에는 task들이 할당된다. Task slot하나당 하나의 thread와 맵핑된다. 하나의 TaskManager는 하나의 JVM 프로세스이고 Task Slot에 할당된 task들은 서로 메모리를 나누어서 사용한다. 여기서 CPU는 공용으로 사용된다.



## Flink Application Execution

### Flink Session Cluster

- Lifecycle : 클라이언트는 항상 실행중인 cluster에 연결하여 job을 제출한다. job이 끝났더라도 클러스터는 종료되지 않는다.
- Resource Isolation : 모든 job이 하나의 cluster에서 실행되므로 클러스터 자원에 대한 경쟁이 발생할 수 있다. Task Manager가 오류가 생기면, 모든 잡들이 실패하게 된다. 또한 JobManager에서 에러가 발생하면 모든 job들에 영향을 주게 된다.
- 사용 usecase : 리소스 할당부터 TaskManager 실행 시간을 상당히 줄여준다. 따라서 job의 실행이 빠르게 처리가 되어야하는경우 사용하면 좋다. 예를들어 데이터 분석가들이 interactive하게 분석하고자할때 유용하다.

> Flink cluster in `session mode` 라고 부르기도 한다.



### Flink Job Cluster

- Lifecycle : YARN과 같은 클러스터 메니저가 클러스터를 실행하며 생성된 클러스터는 특정 job만을 실행한다. 클라이언트가 클러스터 메니저에게 JobManager 실행을 위해 리소스를 요청하고 JobManager의Dispatcher에게 job을 제출한다. Job의 실행이 끝나면 cluster도 종료된다.
- Resource Isolation : JobManager는 Flink job cluster에서 실행중인 특정 job에만 영향을 준다.
- 사용 usecase : Job을 제출하기전에 cluster가 생성되어야 하므로 시간이 소요되지만 long-running large job이나 high-stability가 요구되는 job에 사용하는것이 좋다.



### Flink Application Cluster

- Lifecycle : 하나의 Flink Application에 정의된 job들을 실행하기 위한 전용 클러스터를 띄운다. 즉, 정의된 `main()` 메소드가 클라이언트에서 실행되는것이 아닌 클러스터에서 실행이 된다. 개발자가 직접 클러스터를 수동으로 시작할 필요가 없고, cluster session에 job을 제출할 필요가 없다. 대신 어플리케이션을 JAR Package로 빌드하면 클러스터 entrypoint가 해당 `main()`함수를 실행한다. Flink application을 쿠버네티스의 다른 어플리케이션을 배포하듯이 할수 있고, Flink Application cluster는 Flink application이 종료되면 자동으로 종료된다.
- Resource Isolation : Job cluster와 마찬가지로 하나의 Application이 동립적인 리소스를 할당받는다.
