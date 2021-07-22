---
layout: post
title: "Terraform Introduction"
date: 2021-07-22 13:37:00 +0900
categories: [Terraform]
---

## Terraform

Infrastructure as code(IaC)는 infrastructure를 graphical user interface를 통해서 보다는, configuration 파일들로 관리할수 있게 해준다. 

### Terraform의 장점

- Terraform은 여러 클라우드 플랫폼에 대해서 infrastructure를 관리할 수 있게 해준다.
- human-readable configuration 언어는 infrastructure 코드를 더 빠르게 작성하도록 도와준다.
- Terraform state는 리소스 변화를 deployment를 통해서 추적하게 해준다.
- infrastructure에 대해서 안전하게 협업하기 위해서 version control에 configuration을 커밋할수 있다.

### deployment workflow를 표준화

provider들은 인프라의 개별 unit들을 정의한다.(예를들어, compute instance or private network) 다른 provider들로부터 리소스들을 조합하여 module이라는 재사용이 가능한 Terraform configuration으로 표현가능하다.

Terraform의 configuration 언어는 선언적이며 이는 인프라의 desired end-state를 기술한다. 테라폼은 자동으로 생성할 resource,제거할 resource들 사이의 의존성을 정확한 순서로 파악한다.

![Terraform deployment workflow](https://learn.hashicorp.com/img/terraform/terraform-iac.png)

Terraform으로 인프라를 배포하기 위해서는 :

- Scope - 프로젝트에 대한 인프라를 구명
- Author - 인프라에 대한 configuration 작성
- Initialize - 인프라를 관리하기 위해서 Terraform이 필요한 플러그인을 설치
- Plan - Terraform이 configuration을 매치하기 위해서 적용할 변동사항들을 preview
- Apply - planned 변화들을 만들기