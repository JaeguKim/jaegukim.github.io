---
layout: post
title: "git commands"
date: 2021-01-04 22:42:00 +0900
categories: [Git]
---
## global username, email 설정

``` sh
$ git config — global user.name “Igor Santos”
$ git config — global user.email “igor.santos@example.com”
```

## 직전 commit의 committer name, email 변경

``` sh
git commit --amend --author="[NAME] <EMAIL>"
```

## Git ignore 적용하기
``` sh
git rm -r --cached .
git add .
git commit -m "Apply .gitignore"