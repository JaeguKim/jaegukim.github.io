---
layout: post
title: "Namespace vs Label"
date: 2021-08-17 16:24:00 +0900
categories: [Kubernetes]
---

## Namespace

> 동일한 물리클러스터를 기반으로 여러 가상 클러스터를 지원한다. 이런 가상 클러스터를  Namespace라고 한다.

### 사용해야되는 경우

여러팀에 걸처있는 많은 사용자들을 가진 환경에서 사용한다. 몇십명의 사용자 가지고는 굳이 클러스터를 Namespace를 만들필요가 없다. 리소스의 이름은 Namespace에서 유일해야하고, 하나의 리소스는 하나의 Namespace에 있어야 한다.

약간씩 다른 리소스들을 구별하기 위해서, 여러 Namespace를 사용할 필요는 없다. 같은 Namespace에 있는 자원들을 서로 구별하기 위해서는 Label을 사용하라.
