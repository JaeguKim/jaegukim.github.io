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

## local username, email 설정

``` sh
$ git config --local user.name "jaegoo.kim"
$ git config --local user.email "rlaworn1993@gmail.com"
```

## git config list

``` sh
$ git config --local --list
```

## 직전 commit의 committer name, email 변경

``` sh
git commit --amend --author="[NAME] <EMAIL>"
```

## 이미 push된 커밋 author 변경하기

``` sh
git commit --amend --author="Author Name <email@address.com>"
git push -f
```

## Git ignore 적용하기

``` sh
git rm -r --cached .
git add .
git commit -m "Apply .gitignore"
```

## commit sha 정보 조ㅣ

``` sh
git show [commit sha]
```

## Branch 삭제

- Local branch 
   ``` sh 
   git branch -d [branch_name] 
   ```
- Global branch
   ``` sh
   git branch -D [branch_name1] [branch_name2] ...
   git push [remote_name] --delete [remote_branch_name1] [remote_branch_name2] ...
   ```

## Branch 목록 보기

``` sh
> git branch // local branch 보기
> git branch -r // remote branch 보기
> git branch -a // local,remote 상관없이 보기
```

## submodule

> $ git submodule add [GIT_URL] // Add submodule
> $ git submodule init // set up local config file based on submodule info
> $ git submodule update // pull data from remote repository

## [Stash](https://www.atlassian.com/git/tutorials/saving-changes/git-stash)

 ```git stash``` : The command takes your uncommitted changes (both staged and unstaged), saves them away for later use, and then reverts them from your working copy. 

```git stash pop``` : removes the changes from your stash and reapplies them to your working copy

```git status apply``` : reapply the changes to your working copy and keep them in your stash

```git stash drop``` : delete stash

## Rename branch

`git branch -m [old_name] [new_name]`

## n 번째이전 커밋으로 리셋

``` sh
$ git reset --soft HEAD~n
```

## Delete files in git history

- use [bfg-repo-cleaner](https://rtyley.github.io/bfg-repo-cleaner/)
- [docs](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository)

## merge

``` sh
git checkout <the branch you want to merge into>
git merge <the branch you want contents from>
```

## cherry pick
다른 브랜치에 있는 특정 커밋을 현재 브랜치로 커밋하고 싶을때 보통 다음과 같이 사용한다.

```
git cherry-pick 586030a0c492491b89768436a5ef2d821c6176e6
```

visual studio code의 plugin인 GitLens를 사용하면 아래와같이 손쉽게 cherry picking할수 있다.

![img](https://res.cloudinary.com/practicaldev/image/fetch/s--8qthykM6--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/http://res.cloudinary.com/hackafro/image/upload/v1518728407/Screenshot_9_ip7xnw.png)

## [pop specific file in stash](https://stackoverflow.com/questions/1105253/how-would-i-extract-a-single-file-or-changes-to-a-file-from-a-git-stash)

``` sh
$ git checkout stash@{0} -- <filename>
```

## git squash
여러 커밋을 하나의 커밋으로 묶고 싶을때 사용할 경우가 있는데, 이때 interactive rebase를 사용가능하다.

``` sh
$ git rebase -i HEAD~3 # 최근 3개의 커밋 rebase
```

그리고 나타나는 vi에디터 상에서 나타난대로 수정하면된다.

## 이미 Push된 commit을 squash 한다면, 다음 커멘드를 실행

``` sh
$ git push --force origin master
```

## remote에서 branch 정보 갱신

``` sh
$ git remote update
$ git fetch
```
