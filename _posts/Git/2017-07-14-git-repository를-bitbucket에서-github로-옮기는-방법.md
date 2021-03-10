---
layout: post
title: "git repository를 bitbucket에서 github로 옮기는 방법"
date: 2017-07-14
categories: [Git]
---
1. Make a bare mirrored clone of the repository 
``` sh
git clone --mirror [bitbucket URL]
cd repository-to-mirror.git 
git remote set-url --push origin [github URL]
```
2. Set the push location to your mirror  
``` sh
git push --mirror 
```


