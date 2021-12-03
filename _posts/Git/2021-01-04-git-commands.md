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

## submodule clone

> git submodule init
> git submodule update

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