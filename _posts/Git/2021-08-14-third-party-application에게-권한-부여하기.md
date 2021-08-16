---
layout: post
title: "Third Party Application에게 권한 부여하기"
date: 2021-08-14 14:53:00 +0900
categories: [Git]
---

SmartGit에서 Preferences에서 Github Hosting Provider를 설정하다가, 실수로 organization에 있는 repo에 접근권한을 부여 하지 못했다.

## 수동으로 권한 부여하기

1. 깃헙에 로그인한후 Settings에 들어간다.
2. 왼쪽 바에 Applications 탭을 클릭한다.
3. authorized OAuth App 탭을 누르고, 권한을 부여할 앱을 클릭한다.
4. 해당 앱에게 권한을 부여한다. 