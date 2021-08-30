---
layout: post
title: "PySpark과 Scala 코드를 실행하기 위한 단일 이미지 사용기"
date: 2021-08-30 15:07:00 +0900
categories: [Docker]
---

## PySpark과 Scala app 단일 이미지 사용시 장점

- 하나의 도커이미지만 사용하면 되므로 관리가 간편해진다.

## GCR을 이용하여, 쉽게 빌드하기

Spark official repo에 있는 [도커파일](https://github.com/apache/spark/blob/branch-3.1/resource-managers/kubernetes/docker/src/main/dockerfiles/spark/bindings/python/Dockerfile) 을 빌드하면 되는데, 여기서 base_img를 설정해야 한다. 여기서 base_img는 [도커파일](https://github.com/apache/spark/blob/branch-3.1/resource-managers/kubernetes/docker/src/main/dockerfiles/spark/Dockerfile) 을 빌드한 이미지의 태그를 넘겨주어야 하므로, 해당 도커 파일을 먼저 빌드해야 한다. 

이를 하기위해서는 Spark전체를 빌드해야하는데, 시간이 꽤나 많이걸린다.(i5,8GB 맥북 사양기준으로 1시간정도가 소요된다.) 그렇기 때문에 보통 [GCR](https://console.cloud.google.com/gcr/images/spark-operator/global/spark)에 있는 이미지를 사용하도록 한다.

## 시행착오 및 해결방법

이렇게 빌드하고 나서는 문제점이 한가지가 생긴다. 바로 Scala app을 실행할때 다음의 오류가 발생한다.

```
/opt/entrypoint.sh: line 40: /tmp/java_opts.txt: Permission denied
```

위 에러가 발생하는 이유는 base image에서 마지막 라인에 ``` USER ${spark_uid} ``` 라는 라인에서 ```entrypoint.sh``` 가 실행되어야 하는 유저 아이디를 제한하고 있기 때문이다.

PySpark 도커 이미지를 다음처럼 수정해야 한다.

### 변경 이전

```dockerfile
...
ENTRYPOINT [ "/opt/entrypoint.sh" ]
USER ${spark_uid}
```

### 변경 이후

``` Dockerfile
...
USER ${spark_uid}
ENTRYPOINT [ "/opt/entrypoint.sh" ]
```

## 원인 파악

정확한 원인은 Scala앱이 실행이 될때,  ```entrypoint.sh``` 의 40줄인

``` env | grep SPARK_JAVA_OPT_ | sort -t_ -k4 -n | sed 's/[^=]*=\(.*\)/\1/g' > /tmp/java_opts.txt ```  에서 SPARK_JAVA_OPT_ 값이 NULL이 아니기 때문에 ```/tmp/java_ops.txt``` 까지 실행이 되면서, 권한이 존재하지 않는 파일에 접근하면서 에러가 난것으로 보인다.

PySpark의 경우는 SPARK_JAVA_OPT_ 옵션이 존재하지 않기 때문에 뒤에 있는 커멘드가 실행되지 않은 것으로 보인다.