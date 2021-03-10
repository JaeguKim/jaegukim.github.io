---
layout: post
title: "Kubernetes Compute Resources"
date: 2021-01-16 21:50:00 +0900
categories: [Kubernetes]
---

Kubernetes 에서는 두가지 리소스 타입이 있다.

- Compute resources(CPU, memory)
- API resources(k8s objects - pods, services )
- CPU 단위 : m (1/1000 core)
- Memory 단위  : E,P,T,G,M,K or Ei,Pi,Ti,Gi,Mi,Ki

## Quality of Source(QoS)

kubernetes는 resource request와 limit이 존재하여 pod container가 소모하는 리소스의 양을 조절할수 있게 해준다. 

## Resource request, limit의 동작방식

Kubernetes 스케줄러는 하나의 인스턴스에서 동작하는 컨테이너들의 리소스의 합이 pod에 할당된 리소스를 초과하지 않도록 보장한다. 여기서 request,limit의 차이를 알필요가 있다.

- **Request** 는 쿠버네티스가 pod에 보장할수있는 자원의 양이다.
- **Limit**은 쿠버네티스가 pod이 사용하도록 허락하는 자원의 최대양이다.

pod을 deploy할때, capacity check는 compute resource의 합이 노드가 할당할수 있는 자원의 양을 초과하지 않는지 결정한다.



## Request와 limit이 강요되는 방식

이는 리소스가 compressible인지 incompressible인지에 달려있다. Compressible 자원은 스로틀링 될수있다. 예를들어 CPU는 compressible하고 메모리는 incompressible하다.

pod은 CPU request을 보장받을수 있으며, 다른 pod에 할당된 자원에 따라 더 많은 CPU자원을 받을수도 있고 그렇지 못할수도 있다. 하지만 limit보다 많은 CPU자원은 받을수 없다. 

pod은 Memory request를 보장받을 수는 있지만, memory limit을 초과할때는 가장 많은 메모리를 사용하고있는 컨테이너내의 프로세스는 강제 종료될수 있다.  pod은 종료되지 않지만 container내의 프로세스는 종료될수있다.



## QoS Class

노드가 완전히 compute resource가 소진된 경우가 발생할수 있다. 이러한 극단적인 상황에서 노드에서 실행중인 컨테이너들을 죽여야한다. 이상적으로는 가장 critical하지 않은 컨네이너들부터 제거하여 자원을 확보해야한다. QoS를 이용하여 어떠한 pod이 먼저 제거되어야하는지 설정할수 있다.

세가지 타입의 클래스가 존재한다

- **Best effort**. 아무런 request, limit이 없는 pod. 리소스 소진시, 가장먼저 종료되는 타입이다.

  ``` yaml
  Containers:
    name: foo
      Resources:
    name: bar
      resources:
  ```

  

- **Guaranteed**. request와 limit 값이 동일하게 설정된 pod. 이 pod들은 가장 우선순위가 높으며, 더 낮은 우선순위의 pod이 없을경우에만 종료된다.

  ``` yaml
  containers:
    name: pong
      resources:
        limits:
          cpu: 100m
          memory: 100Mi
        requests:
          cpu: 100m
          memory: 100Mi
  ```

  

- **Burstable**. request와 limit값이 다르게 설정된 pod. **best effort** 타입 pod이 없을경우에 종료된다.

``` yaml
containers:
  name: foo
    resources:
      limits:
        memory: 1Gi

  name: bar
    resources:
      limits:
        cpu: 100m
```

## Ephemeral Volumes
어플리케이션이 실행되고 pod과 함께 생성되고 삭제되는 임시 공간을 의미한다.

## Local ephemeral storage

노드들은 local ephemeral storage(locally-attached writeable device 또는 RAM에 의해서 지원됨)를 가지고 있다. "Ephemeral"은 durability를 장기적으로 보장할수 없음을 의미한다. pod은 ephemeral local storage를 캐싱이나 로그를 저장하기 위하여 사용한다. 

> **주의** : 만약 노드가 실패할때, ephemeral storage에 있는 데이터는 손실될수 있다. 


