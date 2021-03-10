---
layout: post
title: "[Trouble Shooting] Could not find gem 'nokogumbo(~> 2.0)' 해결하기"
date: 2020-12-03 22:13:00 +0900
categories: [etc]
---

Jekyll 엔진 기반의 블로그에 글을 작성하고 커밋을 했더니,
github Actions에서 다음과 같은 에러가 발생하였다.

```
Run bundle install --local
Resolving dependencies...
Bundler could not find compatible versions for gem "nokogumbo":
  In Gemfile:
    html-proofer was resolved to 3.16.0, which depends on
      nokogumbo (~> 2.0)

Could not find gem 'nokogumbo (~> 2.0)', which is required by gem
'html-proofer', in any of the sources.
Error: Process completed with exit code 6.
```

평소에는 잘 되더니 갑자기 안되서 내가 작성한 글에 문제가 있나 싶어 봤더니, 아무리 봐도 원인을 찾을 수 없었다.
결국은 Gemfile에 다음라인을 추가해주었다.

```
gem "nokogumbo", ">=2.0"
```

해결은 되었지만 Gemfile에 있는 모듈들이 의존하고 있는 모듈들이 빠져있는 이슈가 후에도 발생할것 같다는 느낌이 든다.

