---
layout: post
title: "Trouble Shooting(Kubernetes)"
date: 2021-09-08 22:45:00 +0900
categories: [Kubernetes]
---

## pv 또는 pvc가 삭제가 안되고 계속 pending 상태일 경우

1. pv에 바인딩된 Pod을 찾아서 날린다.
2. pv 삭제
3. pvc 삭제

## pod has unbound immediate PersistentVolumeClaims
pvc가 pv에 바인딩 되지 못해서 발생

## ```Error:  `selector` does not match template `labels```
deployment의 spec.selector.matchLabels에 정의 되어있던 ```app.kubernetes.io/component```와 spec.template.metadata.labels에 정의 되어있는 ```app.kubernetes.io/component```가 달라서 발생하였음.
구체적으로는 nginx-ingress-controller 헬름차트 values.yaml에 defaultBackend 정의하는 부분에서 app.kubernetes.io/component를 ```default-backend```로 수정해서 해결하였음.

## Chart conflicts with existing v1beta1.external.metrics.k8s.io resource

external metric api server가 이미 존재하는데 새로 생성하려고 할때 발생
[참고](https://githubmate.com/repo/DataDog/helm-charts/issues/118)

## subchart로 차트 배포시 `Error: found in Chart.yaml, but missing in charts/directory:...`

`helm dependency update .` 실행

## Pod가 아닌 리소스 삭제시 계속 생성되는 경우

argo cd에서 다른 저장소에 있는 차트를 배포하고 있어서 발생
