---
layout: post
title: "Chart Hooks"
date: 2021-12-08 22:20:00 +0900
categories: [Kubernetes]
---

## Chart Hooks

Helm은 차트 개발자들이 release의 life cycle의 특정 시점에 개입하도록 허락하기 위해서 `hook`이라는 메커니즘을 제공한다. 예를들어 다음과 같은 작업이 가능하다.

- 다른 차트가 로드되기 전에 ConfigMap이나 Secret을 로드
- 새로운 차트를 설치하기 전에 DB를 백업하는 job을 실행하고 데이터 복원후에 두번째 job을 실행
- 배포된 차트를 삭제하기 전에, 서비스를 우아하게 종료하기 위한 잡을 실행

## 사용가능한 Hooks

대표적으로 아래와 같은 Hook있다.

- `pre-install` : template이 렌더링된후에 실행되지만, 쿠버네티스에 리소스를 만들기전에 실행된다.
- `post-install` : 모든 리소스들이 쿠버네티스에 로드된 다음에 실행된다.

그밖에 여러 훅들은 아래의 참고 링크를 참고하자.

## Hook deletion policies

언제 hook resource를 삭제할지 결정하는 정책을 정의할 수 있다.

```yaml
annotations:
  "helm.sh/hook-delete-policy": before-hook-creation,hook-succeeded
```

다음과 같은 annotation들이 있다.
- before-hook-creation : 새로운 훅을 실행하기 전에 이전의 리소스 삭제
- hook-succeeded : 훅이 성공적으로 실행되고 나서 리소스 삭제
- hook-failed : 실행도중 훅이 실패하면 리소스 삭제

## [참고](https://helm.sh/docs/topics/charts_hooks/)