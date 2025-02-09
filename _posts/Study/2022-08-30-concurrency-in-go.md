---
layout: post
title: "Concurrency in Go"
date: 2022-08-30 12:16:00 +0900
categories: [Study]
---

## 1. 동시성 소개
- 라이브락이란 프로그램들이 활동적으로 동시에 연산을 수행하고는 있찌만, 이 연산들이 실제로 프로그램의 상태를 진행시키는데 아무런 영향을 주지 못하는 의미 없는 연산 상태를 의미한다.
- 동기화된 메모리 접근에는 비용이 많이 들기 때문에 임계 영역 너머까지 잠금을 확장하는 것이 유리할 수 있다. 반면에 이렇게 하면 다른 동시 프로세스를 기아 상태로 빠뜨릴 위험이 있다.
- 애플리케이션의 성능을 조정해야 할 때가 되면 우선 임계 영역에서만 메모리 접근을 동기화하도록 제한하고 성능에 문제가 되는 경우 언제든 범위를 확장하면 된다.

## 2. 코드 모델링: 순차적인 프로세스 간의 통신
- 채널 vs 뮤텍스
    - 채널을 사용해야 하는 경우
        - 데이터의 소유권을 이전해야 하는 경우
        - 여러 부분의 논리를 조정해야 하는 경우
    - 뮤텍스를 사용해야 하는 경우
        - 성능상의 임계 영역인 경우 : 특정 프로그램 영역이 나머지 부분보다 현저하게 느린 주요 병목 지점으로 밝혀졌다면, 메모리 접근 동기화 기본 요소를 사용하자.
        - 구조체의 내부 상태를 보호해야하는 경우

## 3. Go의 동시성 구성 요소
- RWMutex가 Mutex보다 성능이 좋음.
- `sync.Once`의 `Do`함수는 함수인자에 어떤 함수를 넘기더라도 한번만 호출가능
