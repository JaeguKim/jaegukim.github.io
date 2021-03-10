---
layout: post
title:  "[Spring Boot] Spring 2.x 버전에서 JAR로 Packaging 하는 것에 대하여"
date:   2020-10-26
categories: [Spring]
---
Spring Boot 2.x 버전의 앱을 JAR로 패키징하는데 꽤나 많은 시간을 소비하였는데, 2.x 이전버전의 경우를 시도하다 보니 시행착오를 많이했다. 스택오버플로우 에서 찾아보면서 꼼꼼히 읽는 훈련을 계속 해야겠다.

[해답](https://stackoverflow.com/a/52404325/8276700)은 간단했다.

Spring Boot 2.x 버전에서 bootJar과 bootWar 이라는 gradle task가 app을 패키징하는 역할을 한다.

bootJar task는 실행가능한 jar file을 만드는데 책임을 지고 이는 java plugin이 적용이 될때 자동으로 생성된다고 한다.

따라서 build.gradle 파일에 다음 라인을 추가해야한다.
``` gradle
plugins {

    id 'java'

    id 'org.springframework.boot' version '2.3.4.RELEASE'

}
```
그리고 루트 디렉토리에서 
``` sh
./gradlew bootJar 
```
을 입력하면 build/libs 폴더에 jar 파일이 생성된다.

유사하게 bootWar는 executable war file을 생성하고 war plugin이 적용될때 동작한다.
``` sh
./gradlew bootWar 
```
을 입력하여 실행할수 있다.