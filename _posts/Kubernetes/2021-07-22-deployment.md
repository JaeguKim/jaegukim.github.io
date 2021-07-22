---
layout: post
title: "Deployment"
date: 2021-07-22 11:27:00 +0900
categories: [Kubernetes]
---

## Deployments

Deployment는 Pod과 ReplicaSet에 대한 선언적 업데이트를 제공한다.

Deployment에 desired state 정보를 기술하고, Deployment Controller는 실제 상태를 desired state로 controlled rate로 변경한다. Deployment는 새로운 ReplicaSet을 생성하기 위해서 정의할 수 있다, 또는 이미 존재하는 Deployment를 제공할 수도 있고, 모든 resource들을 새로운 deployment에 적용할 수 있다.

### Use Case

- ReplicaSet을 rollout 하기위해서 Deployment 생성. 
- deployment의 PodTemplateSpec을 업데이트하기 위해서, pod의 새로운 상태를 정의. 
- earlier Deployment revision으로 rollback
- 더 많은 로드를 감당하기 위해서, Deployment를 scale up
- PodTemplateSpec의 여러 수정사항을 반영하기 위해서 Deployment를 중지
- rollout이 막혔는지 확인하기 위해서, Deployment의 status를 사용하기.
- 더이상 필요없는 오래된 ReplicaSet을 청소