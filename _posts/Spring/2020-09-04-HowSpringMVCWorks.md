---
layout: post
title:  "Spring MVC 동작원리"
date:   2020-09-04
categories: [Spring]
---
Spring 동작원리에 대해서 설명한 좋은 글을 발견했다. 이 글을 읽고 내 나름대로 요약해보았다.

[출처 link](https://mystes.tistory.com/81)

![img]({{site-url}}/assets/img/post/Spring/SpringMVC.png)  

1. 사용자가 서버로  request

2. Dispatcher-servlet은 Handler-Mapping에 request를 보내 해당하는 요청의 URL과 일치한 컨트롤러 정보를 요청, Handler-Mapping은 요청에 부합하는 컨트롤러를 탐색하고 리턴

3. Dispatcher-servlet은 그 정보를 통해 컨트롤러와 연결

4. 해당 컨트롤러는 흐름에서 필요한 데이터를 추출하여 요청을 처리하고 다시 Dispatcher-Servlet에게 처리된 데이터와 뷰에 관한 정보를 전달한다. 

5. Dispatcher-servlet은 이러한 정보를 View-Resolver에게 전달하고, View-Resolver는 요청에 부합하는 뷰 객체를 생성하여 데이터를 리턴

6. 해당 뷰에 model 객체를 적용하여 최종적으로 사용자에게 response