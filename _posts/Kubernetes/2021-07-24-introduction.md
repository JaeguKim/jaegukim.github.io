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

  ## Building Your YAML Files

- Kind : we can get a list of resources the cluster supports
  - ``` kubectl api-resources```
- Notice some resources have multiple API's (old vs. new)
- apiVersion : We can get the API versions the cluster supports
  - ``` kubectl api-versions```
- metadata : only name is required
- spec : where are the action is at!

## Storage in Kubernetes

- Storage and stateful workloads are harder in all systems
- Containers make it both harder and easier than before
- StatefulSets is a new resource type, making POds more sticky
- Bret's recommendation : avoid stateful workloads for first few deployments until you're good at the basics
  - Use db-as-a-service whenever you can

## Volumes in Kubernetes

- Creating and connecting Volumes : 2 types
- Volumes
  - Tied to lifecycle of a Pod
  - All container in a single POd can share them
- PersistentVolumes
  - Created at the cluster level, outlives a Pod
  - Seperates storage config from Pod using it
  - Multiple Pods can share them
- CSI plugins are the new way to connect to storage

## Ingress

- None of our Service types work at OSI Layer 7 (HTTP)
- How do we route outside connections based on hostname or URL?
- Ingress Controllers (optional) do this with 3rd party proxies
- Nginx is popular, but Traefix, HAProxy, F5, Envoy, Istio,  etc.

## CRD's and The Operator Pattern

- You can add 3rd party Resources and Controllers
- This extends Kubernetes API and CLI
- A pattern is starting to emerge of using these together
- Operator : automate deployment and management of complex apps
- e.g. Databases, monitoring tools, backups, and custom ingresses

## Higher Deployment Abstractions

- All out ```kubectl``` commands just talk to the Kubernetes API
- Kubernetes has limited built-in templating, versioning, tracking, and management of your apps
- There are now over 60 3rd party tools to do that, but many are defunct
- Helm is the most popular