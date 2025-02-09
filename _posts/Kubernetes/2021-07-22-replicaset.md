---
layout: post
title: "ReplicaSet"
date: 2021-07-22 11:18:00 +0900
categories: [Kubernetes]
---

## ReplicaSet

ReplicaSet의 목적은 주어진 시간에 실행중인 일련의 안정적인 replica pod들을 유지하기 위한 것이다. 동일한 pod들을 명시된 숫자만큼 이용가능하도록 보장하기 위해서 사용된다.

### 동작방식

ReplicaSet은 여러 필드들로 구성이 된다.

- selector : pod들을 규명하는 방법
- a number of replicas : 유지해야하는 pod의 수
- pod template : replicas 수 기준을 충족하기 위해 생성해야하는 새로운 pod의 데이터를 명시

ReplicaSet은 desired number에 도달하기 위해서 pod을 생성하고 제거하면서 이러한 목적을 달성한다. ReplicaSet이 새로운 pod을 생성할 필요가 있을때, pod template를 사용한다.

ReplicaSet은 Pod의 metadata.ownerReference 필드를 통해서 연결된다. 이 필드는 현재 오브젝트가 소유하고 있는 리소스가 무엇인지 명시한다. ReplicaSet에 의해서 획득된 pod들은 OwnerReference 필드 내에서, 자신을 소유하고 있는 ReplicaSet의 정보를 가진다. 이 링크를 통해서 ReplicaSet은 유지하고 있는 pod의 상태를 알고 그에 따라서 계획을 세운다.

ReplicaSet은 selector를 사용해서 획득할 새로운 pod들을 규명한다. 만약 pod이 OwnerReference가 없거나, OwnerReference가 컨트롤러가 아니거나 OwnerReference가 컨트롤러가 아니고 ReplicaSet의 selector와 매칭되면, ReplicaSet에 의해서 즉시 획득된다.

### ReplicaSet을 언제 사용할까?

ReplicaSet은 주어진 시간에 특정 수의 pod replicas가 동작함을 보장한다. 그러나 Deployment는 Replicas를 관리하는 higher-level 개념이고, pod에 대한 declarative update를 제공한다. 그러므로 ReplicaSet을 직접적으로 사용하는 것 대신 Deployment를 사용하는 것을 추천한다. 