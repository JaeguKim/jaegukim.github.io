---
layout: post
title:  "[Trouble Shooting] Spring Maven Project에서 갑자기 api endpoint에 404 error가 뜰때 + Dynamic Web Module to x.x Error in Eclipse"
date:   2020-10-24
categories: [Spring]
---
# Spring Maven Project에서 갑자기 api endpoint에 404 error가 뜰때
Git의  커밋로그를 분석하여 차이가 발생한 부분을 찾아보았다. 프로젝트의 .classfile에 다음 라인이 누락삭제되어서 발생하였다.
``` html
<attribute name="org.eclipse.jst.component.dependency" value="/WEB-INF/lib"/>
```
이 라인이 어쩌다가 누락이 된것인지는 확실치 않지만 잘되던 프로젝트가 갑자기 안될때는 커밋로그를 분석하는게 좋은것같다. 또한 Spring Boot를 쓰면 실수할만한 환경설정들이 줄어든다는것도 느낀다.

# 이클립스에서 `Dynamic Web Module to x.x” Error in Eclipse` 에러 해결하기
1. 먼저 org.eclipse.wst.common.project.facet.core.xml 파일에 ```<installed facet="jst.web" version="y.y"/>``` 부분의 y.y를 x.x로 수정한다.
2. x.x 버전에 맞는  tomcat버전을 세팅한다.
servlet 버전에 맞는 tomcat 버전은 다음에서 확인한다.[LINK](http://tomcat.apache.org/whichversion.html)