---
layout: post
title: "Software Engineering at Google"
date: 2023-10-02 20:12:00 +0900
categories: [Study]
---

## Chapter 1

Time and Change

- Software를 장기적으로 유지보수가능하게 하는 작업은 지속적인 전투(constant battle)이다.

Hyrum's Law

- API의 충분한 사용자가 있는 경우, 주어진 계약에서 무엇을 약속하는지는 중요하지 않다. : 모든 관찰가능한 당신의 시스템의 행위가 다른 누군가에 의해 의존될 것이다.
- 엔트로피의 법칙이 참이지만, 계속 무질서도를 낮출려고 해야하듯이 우리가 개발한 API도 언젠가는 유저의 어플리케이션을 break할것이지만 API에 대한 변화가 그러한 breakage를 해결하고 식별하고 조사하는 어려움을 고려했을때 가치가 있어야한다.
- Programming의 관점에서는 clever는 칭찬이지만, Software Engineering 관점에서는 clever란 비난(accusation)이다.
- 버그해결이든 디자인 전환이든 개발초기단계에 적용하는것이 가장 비용이 적다.
