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

## 주의할 점

다음은 (37.2323,125.12323) 좌표를 기준으로 200m내의 장소를 조회하는 쿼리이다.
``` sql
select * from Place where ST_Distance_Sphere(location,point(37.2323,125.12323)) < 200 
```

만약 데이터가 SRID값이 기본타입이 아닌 다른 타입(eg. WGS84)인 경우, 다음과 같은 에러를 만날 수도 있다.

``` 
Error Code: 3033. Binary geometry function st_distance_sphere given two geometries of different srids: 4326 and 0, which should have been identical.

```

MySQL에 SRID 값을 지정하지 않고 point를 저장할 경우, SRID 값은 기본적으로 0으로 설정이 된다. 쿼리시 SRID값을 명시해줌으로써 해결이 가능하다.

``` sql
select * from Place where 
ST_Distance_Sphere(location,ST_SRID(point(37.4847142,37.5188072),4326)) < 200
```

참고로 SRID 값이란 Spatial Reference Identifier이라 해서 SRS의 식별자이다. SRS는 Spatial Reference System의 약자로 지구타원체를 2차원으로 표현하기 위한 좌표계이다. 3차원 상의 지구타원체를 2차원으로 projection하여 표현하는데, projection방법이 여러가지 존재한다. WGS84의 경우 SRID값은 4326이고, 단순 직교 자표계의 경우 0 이라고 한다.

## 참고

[https://momentjin.tistory.com/136](https://momentjin.tistory.com/136)
[MySQL에서 SRID값을 명시하여 Point 표현하기](https://dba.stackexchange.com/questions/213813/how-do-i-create-a-point-with-an-srid-in-mysql)
