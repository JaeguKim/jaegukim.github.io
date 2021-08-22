---
layout: post
title: "git squash"
date: 2021-08-11 18:59:00 +0900
categories: [Git]
---

여러 커밋을 하나의 커밋으로 묶고 싶을때 사용할 경우가 있는데, 이때 interactive rebase를 사용가능하다.

``` sh
$ git rebase -i HEAD~3 # 최근 3개의 커밋 rebase
```

그리고 나타나는 vi에디터 상에서 나타난대로 수정하면된다.

## 이미 Push된 commit을 squash 한다면, 다음 커멘드를 실행

``` sh
git push --force origin master
```

## [참고](https://meetup.toast.com/posts/39)