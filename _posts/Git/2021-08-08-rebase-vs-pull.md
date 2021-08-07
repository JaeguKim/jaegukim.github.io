---
layout: post
title: "Fetch,Pull,Rebase"
date: 2021-08-08 00:26:00 +0900
categories: [Git]
---

## fetch

> 원격 저장소의 데이터를 로컬에 가져오기만 할때 사용
>
> 최신 커밋 이력은 이름 없는 브랜치로 로컬에 가져오게 됨. 
>
> FETCH_HEAD 라는 이름으로 체크아웃 가능.

## pull

> FETCH + MERGE

## REBASE

현재 ```experiment``` 라는 브랜치에 checkout 한 상태라고 해보자.

이때 ```git rebase master``` 를 수행하면 다음과 같은 일이 일어난다.

먼저 experiment와 master의 공통 커밋으로 이동하고 나서, 그 커밋부터 지금 checkout 한 브랜치가 가리키는 커밋까지 diff를 차례로 만들어 어딘가에 임시로 저정해 둔다. 그리고 experiment가 master를 가리키는 커밋을 가리키게 하고 아까 저장해 놓았던 변경사항을 차례대로 적용한다. 

![`C4`의 변경사항을 `C3`에 적용하는 Rebase 과정.](https://git-scm.com/book/en/v2/images/basic-rebase-3.png)

>REBASE의 위험성
>
>rebase를 할때, 이미  public repo에 push된 커밋을 대상으로 rebase를 해서는 않된다. 현재 작업을 하고있다는, 다른 사람이 강제로 이미 푸시된 커밋을 대상으로 rebase를 하고, 서버의 히스토리를 덮어씌운 상황을 생각해보자.(```push --force``` 명령어 사용) 이때는 중복된 커밋이 여러개 존재할수 있다.(왜냐하면, rebase한 경우에는 기존에 master에 푸시된 커밋과 동일하지만 다른 커밋이 생성되기 때문이다.) 애초에 서버에 코드를 푸시할때 rebase를 했어야 되었던 것이다.
>
>[참고](https://git-scm.com/book/ko/v2/Git-%EB%B8%8C%EB%9E%9C%EC%B9%98-Rebase-%ED%95%98%EA%B8%B0)

## REBASE vs MERGE

rebase의 장점은 좀더 깨끗한 히스토리를 만든다. 단점은 수많은 merge 커밋이 사라진다는 단점이 있다.

merge의 장점은 정확이 있었던 작업 기록을 좀더 자세히 알수 있다. 머지 커밋이 기록이 남게 되어, 히스토리가 좀 지저분해진다.

## REBASE 순서

``` sh
(사전에 작업한 내용 commit)
git fetch [rebase 할 branch]
git rebase [rebase 할 branch]
git push origin master
```

## 요약

git 공식문서의 일반적인 해답을 정리하자면, 어딘가에 push로 내보낸 커밋에 대해서는 절대 rebase를 하지 말아야 한다.

## [출처](https://git-scm.com/book/ko/v2/Git-%EB%B8%8C%EB%9E%9C%EC%B9%98-Rebase-%ED%95%98%EA%B8%B0)


