---
layout: post
title: "Helm Chart"
date: 2021-07-23 11:08:00 +0900
categories: [Kubernetes]
---

## Helm Chart

### 세가지 큰 개념

Chart는 Helm package이다. 이는 어플리케이션,tool, 또는 서비스를 쿠버네티스 클러스터에서 실행하기 위한 모든 리소스 정의들을 포함한다. 이를 쿠버네티스의 Hombrew formula라고 볼수 있다.

Repository는 chart가 수집되고 공유되는 장소이다. 이는 Perl의 CPAN archive와 유사하거나 Fedora Package Database와 유사하지만 쿠버네티스 패키지라는것이 차이다.

Release는 쿠버네티스 클러스터에서 실행중인 차트의 instance이다. 한개의 차트는 같은 클러스터에 여러번 설치될 수 있다. 설치될때마다, 새로운 release가 생성된다. MySQL 차트를 생각해보면, 클러스터에 2개의 데이터베이스가 실행중이라면, 차트를 두번 설치할 수 있다. 각각은 자신만의 release, release name이 있다.

이러한 개념을 가지고 Helm을 다음과 같이 설명할 수 있다.

> 헬름은 차트를 쿠버네티스에 설치하고, 각각의 installation에 대해서 새로운 release를 생성할 수 있다. 새로운 차트를 찾기 위해서, Helm chart repositories를 검색할 수 있다.

### Helm Dependency란?

[link](https://kb.novaordis.com/index.php/Helm_Dependencies)

- 장점 :chart의 templates 파일들을 다운받을 필요없이 values.yaml만 가지고 argoCD에 배포가능

## Commands

- repo 추가 및 업데이트 : `helm repo add [repo-name] [repo-url]`

- 특정 repo에 있는 helm chart download : `helm pull [repo]/[chart-name] --version [version]`