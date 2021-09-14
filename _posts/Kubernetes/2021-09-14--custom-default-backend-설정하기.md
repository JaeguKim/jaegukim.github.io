---
layout: post
title: "custom error page 띄우기"
date: 2021-09-14 15:59:00 +0900
categories: [Kubernetes]
---

## Intro
custom error page를 띄우기 위해서, nginx-ingress-controller 차트에 custom default backend를 설정해야한다.
custom-default-backend는 nginx-ingress-controller에서 발생한 http error를 대신 처리해줄 리소스를 의미한다.
이때 custom-default-backend에 컨테이너 이미지를 설정해주어야 한다.

## 1. Dockerfile 빌드후 푸시하기
1. 먼저 아래의 도커파일을 생성한다.
``` Dockerfile
FROM quay.io/kubernetes-ingress-controller/custom-error-pages-amd64:0.4

COPY content /www
```
2. content 디렉토리 생성후, 원하는 에러페이지를 위치시킨다. 예를들어 403.html, 503.html 등등을 위치시킨다.
3. 도커파일을 빌드후 푸시한다.

## 2. ingress-nginx-controller에 defaultBackend 적용하기
아래 두가지 use-case에 따라서 defaultBackend를 설장할 수 있다.
여기서는 version ```3.34.0```, appVersion: ```0.47.0```을 기준으로 설명한다.

### 2-1. 전체 namespace에 있는 Ingress에 대해서 default backend 지정하고 싶은 경우
nginx-ingress-controller 헬름차트를 아래와 같이 수정한다. 
1. ```controller-configmap.yaml```에 아래라인을 추가한다.
``` yaml
{{- if .Values.defaultBackend.enabled }}
custom-http-errors: {{ .Values.defaultBackend.customHttpErrors }}
{{- end }} 
```
2. values.yaml에서 defaultBackend을 다음과 같이 수정한다. 
``` yaml
## Default 404 backend
##
defaultBackend:
##
enabled: true

name: defaultbackend
image:
    registry: [enter your registry name]
    image: [enter your image]
    # for backwards compatibility consider setting the full image url via the repository value below
    # use *either* current default registry/image or repository format or installing chart by providing the values.yaml will fail
    # repository:
    tag: [enter your tag]
    pullPolicy: IfNotPresent
    # nobody user -> uid 65534
    runAsUser: 65534
    runAsNonRoot: true
    readOnlyRootFilesystem: true
    allowPrivilegeEscalation: false

customHttpErrors: [error code to override eg. 403,404,503]
# Use an existing PSP instead of creating one
existingPsp: ""

extraArgs: {}

serviceAccount:
    create: true
    name: ""
    automountServiceAccountToken: true
## Additional environment variables to set for defaultBackend pods
extraEnvs: []

port: 8080

## Readiness and liveness probes for default backend
## Ref: https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-probes/
##
livenessProbe:
    failureThreshold: 3
    initialDelaySeconds: 30
    periodSeconds: 10
    successThreshold: 1
    timeoutSeconds: 5
readinessProbe:
    failureThreshold: 6
    initialDelaySeconds: 0
    periodSeconds: 5
    successThreshold: 1
    timeoutSeconds: 5

## Node tolerations for server scheduling to nodes with taints
## Ref: https://kubernetes.io/docs/concepts/configuration/assign-pod-node/
##
tolerations: []
#  - key: "key"
#    operator: "Equal|Exists"
#    value: "value"
#    effect: "NoSchedule|PreferNoSchedule|NoExecute(1.6 only)"

affinity: {}

## Security Context policies for controller pods
## See https://kubernetes.io/docs/tasks/administer-cluster/sysctl-cluster/ for
## notes on enabling and using sysctls
##
podSecurityContext: {}

# labels to add to the pod container metadata
podLabels: {
    helm.sh/chart: ingress-nginx-3.34.0,
    app.kubernetes.io/name: ingress-nginx,
    app.kubernetes.io/instance: ingress-nginx,
    app.kubernetes.io/version: 0.47.0,
    app.kubernetes.io/managed-by: Helm,
    app.kubernetes.io/component: default-backend
}
#  key: value
```

### 2-2. Ingress 별로 default backend 지정하고 싶은 경우
1. [링크](https://medium.com/alterway/how-to-custom-your-default-backend-on-kubernetes-nginx-controller-9b38048e10c0)를 참고해서 default backend 리소스를 Ingress가 존재하는 네임스페이스에 리소스를 생성한다.
2. Ingress 리소스 annotation에 custom-http-errors와 default-backend 설정을 추가한다.
예시는 아래와 같다.
``` yaml
//403 error에 대해서 default-http-backend라는 서비스를 사용함을 의미한다.
"nginx.ingress.kubernetes.io/custom-http-errors": "403",
"nginx.ingress.kubernetes.io/default-backend": "default-http-backend"
```

## 참고
[https://kubernetes.github.io/ingress-nginx/examples/customization/custom-errors/](https://kubernetes.github.io/ingress-nginx/examples/customization/custom-errors/)
[https://kubernetes.github.io/ingress-nginx/user-guide/custom-errors/](https://kubernetes.github.io/ingress-nginx/user-guide/custom-errors/)
[https://stackoverflow.com/questions/60233958/how-to-customize-error-pages-served-via-the-default-backend-of-an-nginx-ingress](https://stackoverflow.com/questions/60233958/how-to-customize-error-pages-served-via-the-default-backend-of-an-nginx-ingress)