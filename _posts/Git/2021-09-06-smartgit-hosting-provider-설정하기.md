---
layout: post
title: "SmartGit Hosting Provider 설정하기"
date: 2021-09-06 22:42:00 +0900
categories: [Git]
---

SmartGit으로 특정 Organization에 있는 리포에 푸시할때, 디폴트로 github id,pw로 인증을 하라는 팝업이 뜰때가 있다.
id,pw로 인증하는 방식은 더이상 사용되지 않기 떄문에 사용하면 않된다.

## 해결방법
1. Preference -> Hosting Provider 에서 + 버튼 클릭후, token을 생성한다.
    - 이때 github organization에 third party applicationd에게 권한을 부여해야 한다.(이 과정은 보이는 팝업 그대로 따라하면 된다.)
2. OK 버튼을 누른다.