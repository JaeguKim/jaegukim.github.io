---
layout: post
title: "Git guide from fork to pr"
date: 2021-08-22 16:28:00 +0900
categories: [Git]
---

## Git step by step guide

### 1. Clone Repository

1. Go to origin repository and fork

2. Go to [username]/[repository name]

3. clone forked repository 

   ``` sh
   git clone [fored repo address]
   ```

4. set remote repository as upstream

   ``` sh
   git remote add upstream [original repo address]
   ```

### 2. [Recommend] Make and checkout  new branch 

``` sh
git checkout -b [branch name]
```

### 3. How to PR

1. Sync forked repository with original repository

2. Go to origin repository and make pull request

3. Delete local branch after pr is merged

   ``` sh
   git 
   ```

   

## Appendix

### How to sync fored repoitory With original repository

``` sh
git checkout [main or master]
git fetch upstream
git rebase upstream/[branch you want to sync with]
git push origin [main or master]
```

``` sh
git checkout [main or master]
git fetch upstream
git push
git stash save --keep-index
git stash drop
```