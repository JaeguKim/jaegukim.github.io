---
layout: post
title: "DinD vs DooD"
date: 2021-10-17 11:49:00 +0900
categories: [Docker]
---

## DinD (Docker in Docker)
- 도커 컨테이너 내에서 추가적인 도커 데몬을 실행하는 방식
- ` docker run --privileged --name dind1 -d docker:20.10.5-dind` 명령어를 실행해서 생성하는 `--privileged` 옵션은 호스트의 모든 장치에 액세스하는 권한을 부여함.
- 단점 : 컨테이너가 호스트의 컨테이너 외부에서 실행되는 프로세스와 거의 동일한 호스트 액세스를 허용하므로 보안상으로 안전하지 않다.

## DooD (Docker out of Docker)
도커 컨테이너에서 호스트의 도커 데몬을 사용하는 방식
- 장점 : DinD에 비해서 좀더 보안상으로 공격받기 어렵다.
- 단점 : 호스트의 자원을 공유할 수 있으므로 이 방법또한 안전하지는 않다.