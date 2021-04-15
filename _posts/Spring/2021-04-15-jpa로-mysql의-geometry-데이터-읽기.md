---
layout: post
title: "JPA로 MySQL의 Geometry 데이터 읽기"
date: 2021-04-15 20:46:00 +0900
categories: [Spring]
---

## JPA로 MySQL의 Geometry 데이터 읽기

> Geographic data(Point,Line,Polygon etc) 는 JDBC specification에 없기 때문에 JTS(Java Topology Suite)를 사용하거나, Geolatte-geom를 사용하여 데이터를 읽을 수 있다. 두 라이브러리 모두 ```hibernate-spatial``` 에 포함되어 있다. 

### 1. Gradle dependency 설정

``` groovy
dependencies {
  ...
    implementation 'org.springframework.boot:spring-boot-starter-data-jpa:2.3.4.RELEASE'
    implementation group: 'org.hibernate', name: 'hibernate-core', version: '5.4.20.Final'
    implementation group: 'org.hibernate', name: 'hibernate-spatial', version: '5.4.20.Final'
...
}
```

세가지를 라이브러리를 추가해준다.

### 2. Application.yml 파일 설정

다음과 에러가 발생할 경우, 

```
org.springframework.orm.jpa.JpaSystemException: could not deserialize; nested exception is org.hibernate.type.SerializationException: could not deserialize
```

```application.yml``` 파일을 다음과 같이 설정해두어야한다.

``` yaml
spring:
	jpa:
		database: mysql
		database-platform: org.hibernate.spatial.dialect.mysql.MySQL56InnoDBSpatialDialect
		# 또는 org.hibernate.spatial.dialect.mysql.MySQL56SpatialDialect 를 사용해도 좋다.
```

```MySQL56SpatialDialect``` 는 ```MySQL55Dialect``` 를 상속하며 spatial data type과 관련된 추가적인 기능을 제공한다.

## 참고

[https://momentjin.tistory.com/136](https://momentjin.tistory.com/136)