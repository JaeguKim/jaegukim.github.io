---
layout: post
title: "CORS setting"
date: 2021-09-25 17:12:00 +0900
categories: [Kubernetes]
---

## nginx controller cors setting
[참고](https://kubernetes.github.io/ingress-nginx/user-guide/nginx-configuration/annotations/#enable-cors)

### example
``` yaml
apiVersion: networking.k8s.io/v1beta1
kind: Ingress
metadata:
  name: {{ .Values.ingress.name }}
  annotations:
    kubernetes.io/ingress.class: nginx
    nginx.ingress.kubernetes.io/force-ssl-redirect: "true"
    nginx.ingress.kubernetes.io/whitelist-source-range: "{{ .Values.cidrWork }},{{ .Values.cidrGithub }},{{ .Values.cidrSmith }},{{ .Values.cidrInternals }}"
    nginx.ingress.kubernetes.io/enable-cors: "true"
    nginx.ingress.kubernetes.io/cors-allow-origin: "https://{{ .Values.ingress.appOriginName }}"
    nginx.ingress.kubernetes.io/cors-allow-headers: "Authorization,Referer,sec-ch-ua,sec-ch-ua-mobile,sec-ch-ua-platform,User-Agent,X-Organization,Content-Type"
```