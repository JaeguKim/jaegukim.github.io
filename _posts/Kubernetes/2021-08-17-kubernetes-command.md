---
layout: post
title: "kubernetes command"
date: 2021-08-17 15:36:00 +0900
categories: [Kubernetes]
---

## Commands

- Pod list

> kubectl get pods --namespace=spark-operator

- Pod에 대한 상세정보

> kubectl describe pod spark-operator-57f8dbcbd6-4tz68

- Pod yaml definition

> kubectl get pod --namespace=spark-operator spark-operator-57f8dbcbd6-4tz68 -o yaml

- List ReplicaSet

> kubectl get rs -n notebook
> -n 는 --namespace 대신 사용할수 있다.

- create resource

> kubectl create -f [file name]

- list service 

> kubectl get svc

- Run bash in Pod Container

> kubectl exec -it [pod name] bash

- print log in Pod

> kubectl logs -f [pod name]

- print log in container of Pod

> kubectl logs -f [pod name] -c [container name]

- Update resource

> kubectl apply -f [file name]

- Check kubernetes version

아래 커멘트 입력후 Server version 필드안에 Git version을 확인한다.
> kubectl version

- Access Service with port-forward in local

> kubectl port-forward [pod-name] [port]:[port] -n [namespace]

- helm templating

> helm template .

- update helm dependency

> helm dependency update .

- switch context

> kubectl config use-context [context name(eg. minikube)]

- delete context

> k config delete-context [context name(eg. minikube)]

- k9s log info

> k9s info

- helm chart 버전 확인하기
``` sh
$ helm repo add bitnami https://charts.bitnami.com/bitnami
$ helm search repo bitnami
```
