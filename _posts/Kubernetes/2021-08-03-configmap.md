---
layout: post
title: "ConfigMap"
date: 2021-08-03 11:36:00 +0900
categories: [Kubernetes]
---

## ConfigMaps

key-value pairs에 non-confidential data를 저장하는데 사용되는 API object이다. Pod들은 ConfigMaps을 환경변수, 커멘드라인 인자, 또는 볼륨에대한 configuration file로 소비할수 있다.

ConfigMap은 environment-specific configuration를 컨테이너 이미지들과 불리하는데 사용될 수 있다. 결과적으로 애플리케이션이 포팅되기 쉬워진다.

>주의 : ConfigMap은 secrecy나 encryption을 제공하지 않는다. 만약 저장하고자하는 데이터가 기밀이라면, ConfigMap 보다는 추가 third party 툴 또는 Secret을 사용하는 것이 좋다. 

### Motivation

application 코드로부터 configuration 데이터를 분리하여 설정하기 위해서 ConfigMap을 사용해라.

예를들어, 로컬에도 실행할 수 있고 클라우드에서 실행할수 있는 어플리케이션을 개발하고 있다고 가정해보자. 만약 ```DATABASE_HOST``` 라는 환경변수를 코드에서 사용하고자 한다고 해보자. 로컬에서는 해당 변수를 ```localhost``` 로 설정할 것이다. 클라우드에서는 클러스터에 대한 데이터베이스 컴포넌트를 노출하는 쿠버네티스 서비스를 가리킬수 있도록 설정할 것이다. 

ConfigMap은 대량의 chunks of data를 수용하도록 설계되지 않았다. ConfigMap에 저장된 데이터는 1MiB를 초과할 수 없다. 만약 제한 범위보다 더 큰 store setting이 필요하다면, mounting volume 이나 독립적인 데이터 베이스나 파일 서비스 사용을 고려해야 한다.

