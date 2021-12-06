---
layout: post
title: "Trouble shooting(Fast API)"
date: 2021-11-21 16:04:00 +0900
categories: [FastAPI]
---

## 307 temporary redirect

- 원인 : endpoint 마지막에 "/" 가 있으면 redirect 하게 되어있어서 발생
- 해결방법
    - endpoint 마지막에 붙어있는 "/" 제거
    - 바꿔야할 endpoint가 많다면,
    ``` python 
        app = FastAPI()
        app.router.redirect_slashes = False
    ```
- [출처](https://somjang.tistory.com/entry/FastAPI-307-temporary-redirect-%ED%95%B4%EA%B2%B0-%EB%B0%A9%EB%B2%95-Python)

## Asyncio 모듈 테스트 중, `Pytest: runtimeerror there is no current event loop in thread 'mainthread'`

- 해결방법 : method위에 `@pytest.mark.anyio` 사용하는 대신, `@pytest.mark.asyncio` 사용하기