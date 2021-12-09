---
layout: post
title: "Prometheus"
date: 2021-12-09 13:35:00 +0900
categories: [DevOps]
---

## Prometheus란?
원래 SoundCloud에서 빌드된 오픈소스 monitorring,alerting toolkit
Prometheus는 time series data로 메트릭을 수집및 적재한다. 즉, 메트릭정보는 label이라고 불리는 optional key-value와 함께 기록된 시간이 저장된다.

### Features
프로메테우스의 기본 기능은 :
- 메트릭 이름과 key-value 쌍으로 식별되는 time series 데이터를 가진 multi-dimensional data model
- PromQL라는 dimensionality를 leverage하기 위한 flexible query language를 사용한다.
- 분산 저장소에 의존하지 않음; 단일 서버 노드들은 autonomous하다(스스로 자신을 제어한다).
- time series 수집은 HTTP를 통해서 모델을 model을 pull한다.
- time series 데이터를 푸시하는 것은 intermediary gateway를 통해서 지원된다.
- 타깃은 service discovery 또는 static configuration을 통해서 발견된다.
- 다양한 모드의 graphing, dashboarding 지원

### Metric이란?

메트릭이란 말그대로 numeric mesurements이며, time series란 변화가 계속해서 기록된다는 의미이다. 유저가 측정하고 싶어하는 것은 어플리케이션에 따라서 다르다. 웹서버에서는 request time일수도 있고, 데이터베이스 에서는 활성화된 커넷션들 또는 active queries일수도 있다.

Metric은 애플리케이션이 왜 특정방식으로 자동이 되는지 이해하는데 있어서 중요한 역할을 한다.



### Components

프로메테우스 ecosystem은 여러개의 컴포넌트로 구성이 되는데, 많은 경우 optional이다.

- time series data를 scrape하고 저장하는 main Prometheus server
- 애플리케이션 코드를 instrumenting하기 위한 client libraries
- short-lived jobs을 지원하기위한 push gateway
- HAProxy, StatsD, Graphite 등과 같은 서비스들에 대한 special-purpose exporters
- alert들을 핸들하기 위한 alertmanager
- 다양한 support tool들

대부분의 프로메테우스 컴포넌트들은 Go로 작성되었고, static binary로 빌드하고 배포하기 쉽게한다.



### Architecture

다음 다이어그램은 프로메테우스와 ecosystem 컴포넌트들의 아키텍쳐이다.

![Prometheus architecture](https://prometheus.io/assets/architecture.png)

프로메테우스는 short-lived job들을 위한 intermediary push gateway를 통해서 또는 직접적으로 instrumented job 메트릭을 수집한다. 모든 scraped sample들을 로컬로 저장하고 존재하는 데이터로 부터 새로운 time series를 기록하고 집계하기 위한 rule들을 실행하거나 또는 알람을 생성한다. Grafana 또는 다른 API 컨슈머들은 수집된 데이터를 시각화하기 위해서 사용된다.



### 언제 적합한가?

프로메테우스는 순수 numeric 타임 시리즈들을 기록하는데 매우 적합하다. machine-centric monitoring 뿐만 아니라 highly dynamic service-oriented 아키텍쳐를 모니터링하는데 적합하다. 마이크로서비스 세계에서, multi-dimensional data 수집과 쿼리를 지원하는것에 강점을 보인다.

프로메테우스는 reliability을 위해서 디자인되었다, 장애가 발생한동안 빠르게 문제를 진단할수 있도록 디자인되었다. 각각의 프로메테우스 서버는 독립적이다.(network storage 또는 다른 remote 서비스들에 대해서 의존하지 않는다.) 



### 언제 적합하지 않은가?

프로메테우스는 repliability에 중점을 둔다. 실패 조건들에서도 항상 당신의 시스템에서 어떤 statistics가 이용가능한지 보여준다. 만약 100%정확성이 필요하다면, 예를들어 per-request billing 같은 경우, 프로메테우스는 적합하지 않은데 왜냐하면 수집된 데이터가 충분히 세부적이고 완전하지 않기 때문이다. 그러한 경우 billing 데이터를 수집하고 분석하기 위해서 다른 시스템을 사용하는것이 더 낫고 프로메테우스는 모니터링 목적으로 사용하는것이 좋다.