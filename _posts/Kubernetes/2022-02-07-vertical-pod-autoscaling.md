---
layout: post
title: "Vertical Pod autoscaling"
date: 2022-02-07 11:45:00 +0900
categories: [Kubernetes]
---

## Overview

CPU와 메모리의  request와 limit을 최신으로 수동으로 업데이트 하는 대신, recommended 값을 제공하거나 자동으로 해당 값으로 업데이트 하도록 설정한다.

## Benefits

- 클러스터 노드들이 효율적으로 운용된다.

- CPU와 Memory request들에 대한 정확한 값을 결정하는데 시간을 들일 필요가 없다.

## Limitations

- 리소스 사용량이 급격히 증가한다고 해서 리소스 추천을 해주진 않고, 좀더 오랜 기간에 걸쳐 안정적인 추천을 해준다. 급격한 증가에 기반을 두어 autoscaling 하려면 HPA를 사용해야 한다.

- maximum 500개의 `VerticalPodAutoscaler` 객체를 지원한다.

- VPA는 아직 JVM 기반의 workload와 사용할수 없다. (workload memory visibility 제한 문제 때문이다.)
