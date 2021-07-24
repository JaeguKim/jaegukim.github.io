---
layout: post
title: "Introduction"
date: 2021-07-24 17:48:00 +0900
categories: [Kubernetes]
---

## Basic Terms : System Parts

- Kubernetes : 전체 orchestration system
- K8s "k-eights" or Kube 라 부름
- Kubectrl : CLI to configure Kubernetes and manage apps
- Node : Kubernetes cluster에 있는 단일 서버
- Kubelet : Kubernetes agent running on nodes
- Control Plance : Set of containers that manage the cluster
  - API server, scheduler, controller manager, etcd 등을 포함
  - 때때로 master라고 불림

## Kubernetes Container Abstractions

- Pod : one or more containers running together on the Node
  - Basic unit of deployment. Containers are always in pods
- Controller : For creating/updating pods and other objects
  - Many types of Controllers inc. Deployment, ReplicaSet, StatefulSet, DaemonSet, Job, CronJob, etc.
- Service : network endpoint to connect to a pod
- Namespace : Filtered group of objects in cluster
- Secrets, ConfigMaps and more

## Three Management Approaches

- Imperative commands : run, expose, scale, edit, create, deployment
  - Best for dev/learning/personal projects
  - Easy to learn,  hardest to manage over time
- Imperative objects : create -f file.yml, replace -f file.yml, delete ...
  - Good for prod of small environments, single file per command
  - Store your changes in git-based yaml files
- Declarative objects : apply -f file.yml or dir\, diff
  - Best for prod, easier to automate
  - Harder to understand and predict changes
- Most Important Rule:
  - Don't mix the three approaches
  - Store yaml in git, git commit each change before you apply
  - This trains you for later doing GitOps(where git commits are automatically applied to clusters)