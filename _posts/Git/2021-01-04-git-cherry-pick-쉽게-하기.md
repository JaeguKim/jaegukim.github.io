---
layout: post
title: "git cherry pick 쉽게 하기"
date: 2021-01-04 22:35:00 +0900
categories: [Git]
---

다른 브랜치에 있는 특정 커밋을 현재 브랜치로 커밋하고 싶을때 보통 다음과 같이 사용한다.

```
git cherry-pick 586030a0c492491b89768436a5ef2d821c6176e6
```

visual studio code의 plugin인 GitLens를 사용하면 아래와같이 손쉽게 cherry picking할수 있다.

![img](https://res.cloudinary.com/practicaldev/image/fetch/s--8qthykM6--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/http://res.cloudinary.com/hackafro/image/upload/v1518728407/Screenshot_9_ip7xnw.png)

## 출처
[https://dev.to/iamafro/how-to-merge-a-specific-commit-into-another-branch--oak](https://dev.to/iamafro/how-to-merge-a-specific-commit-into-another-branch--oak)
