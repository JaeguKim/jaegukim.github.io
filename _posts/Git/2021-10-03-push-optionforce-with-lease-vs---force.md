---
layout: post
title: "push option(force-with-lease vs --force)"
date: 2021-10-03 00:42:00 +0900
categories: [Git]
---

## force-with-lease vs force
공식문서를 참고하면 아래와 같다.

`--force-with-lease` alone, without specifying the details, will protect all remote refs that are going to be updated by requiring their current value to be the same as the remote-tracking branch we have for them.

로컬 리포에 있는 remote ref와 remote repo에 있는 remote ref가 같은 경우에만, force push를 허용한다.

반면 `-force`는 그냥 덮어쓴다.

`--force-with-lease`를 사용하면 remote에 새로운 커밋이 있다는것을 덮어쓰기 전에 확인할 수 있다.

## 참고
- [https://stackoverflow.com/questions/30542491/push-force-with-lease-by-default/43726130#43726130](https://stackoverflow.com/questions/30542491/push-force-with-lease-by-default/43726130#43726130)
