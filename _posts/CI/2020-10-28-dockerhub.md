---
layout: post
title:  "[Travis CI] docker image 빌드하여 dockerhub에 푸시작업 자동화하기"
date:   2020-10-28
categories: [CI]
---
# **1) 프로젝트 루트폴더에 .travis.yml 파일을 생성한다.**

# **2) .travis.yml 파일을 다음과 같이 작성한다.**
``` yml
dist: trusty
env:
  global:
  - DOCKER_USER="USERNAME"
  - DOCKER_PASS="PASSWORD"
jobs:
  include:
  - stage: build safe-place images and push to dockerhub repository
    script:
    - echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
    - docker build --tag kimwithglasses/safe-place-db:0.0.1 . && docker push kimwithglasses/safe-place-db
    - cd SafePlaceAPI && ./gradlew bootJar && docker build --tag kimwithglasses/safe-place-api:0.0.1
      . && docker push kimwithglasses/safe-place-api
```
- dockerhub에 로그인
``` sh
echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin  
```
- 현재 경로에 있는 DOCKERFILE build & push
``` sh
docker build --tag kimwithglasses/safe-place-db:0.0.1 . && docker push kimwithglasses/safe-place-db
```
- 경로 이동하여 gradle project build & push
``` sh
cd SafePlaceAPI && ./gradlew bootJar && docker build --tag kimwithglasses/safe-place-api:0.0.1 .  && docker push kimwithglasses/safe-place-api
```
# **3) 위의 경우는 password가 노출되어있기 때문에 암호화를 진행하였다.**
    1. travis.yml이 있는 경로로 이동
    2. DOCKER_PASS 변수 암호화
    ``` sh
    travis encrypt DOCKER_PASS="password" --add --com
    ```

# **4) 최종 완성된 .travis.yml 파일의 모습은 다음과같다.**
``` yml
dist: trusty
env:
  global:
  - DOCKER_USER=kimwithglasses
  - secure: AEEIHpGihnGMPyUUf5LosnuoXJiJlRiAhiPpSiXmw+tG2TQRj+O92gnmOsZ8mnrOs54WbE7ECorBgDSCbdKFAEL6MFfqwIlXQgrucvAYaybk9Oo2eO6Gv9NQPKPgQS6O4ZHacEWncZz9ektk8XQsMjdvnvVgSTL8QYo9mQIqoqB1hZYrRRdKaXOqjnuK/zjryqS2xwtbHyJh3KNLPt3qzUqPYI/eKqa7QgiK5uLJp2uTPy4/ipbEuvxYZzZsF44sRBiqvQhsQ7Xo1xuv3bGGmhRS+NO8mbJF6egZZear+QzaRGqx5G3PZ7CY1sTpSkzwE56h0jXy2BRciClItJ4CNXdH4wf2MK9qsyY5lwY6u2+A4lHnz170UCs/G2tCY6qEg5mkVcf9XOd2D2cJaHW+eyHhta0SjRLOsOEYk2K1qS3FBqm1LGTHqNSx5VWQDVk78Wg7fu7M9TZpgjx0YTpjhaeEQKnmh+3VGn44CEdzn0lCOjPFDUujlidZOZ1dYcRAPSgh7JcGQqNuHCBQVr5LCJkeNtIalwvzPC96oQzLkl7tqYCJc+yIvTng9jPlHzS6zqV8lI6twOkHxvXxo9GvmLaT7Vm6zjfJqCLdWhsX8Sl4DBiHPQb8cQ/576EtznKYYrr6LuX+QVWwsW+ns09LqnmOTtxzNIz7BK3O/Kbr1ts=
jobs:
  include:
  - stage: build safe-place images and push to dockerhub repository
    script:
    - echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
    - docker build --tag kimwithglasses/safe-place-db:0.0.1 . && docker push kimwithglasses/safe-place-db
    - cd SafePlaceAPI && ./gradlew bootJar && docker build --tag kimwithglasses/safe-place-api:0.0.1
      . && docker push kimwithglasses/safe-place-api
```