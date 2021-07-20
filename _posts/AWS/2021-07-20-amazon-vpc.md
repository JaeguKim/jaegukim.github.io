---
layout: post
title: "Amazon VPC"
date: 2021-07-20 11:17:00 +0900
categories: [AWS]
---

## Amazon VPC 

> Amazon Virtual Private(Amazon VPC)는 virtual network에서 AWS 리소스들을 실행하도록 해준다. virtual network는 자신만의 데이터 센터에서 구축된 전통적인 네트워크와 유사하다. AWS의 scalable 인프라를 사용할 수 있다는 장점이 있다.

## Amazon VPC concepts

Amazon VPC는 Amazon EC2의 네트워킹 레이어이다. 

중요한 컨셉은 아래와 같다.

- Virtual Private Cloud(VPC) - AWS account에 할당된 virtual network
- Subnet - VPC내에 있는 IP 주소의 범위
- Route table - 네트워크 트레픽이 어디로 향할지 결정하기 위해 사용되는 일련의 규칙(routes라고 불림)
- Internet Gateway - VPC와 인터넷에 있는 리소스들 간의 커뮤니케이션을 가능하게 하기 위해서 VPC에 붙어있는 gateway
- VPC endpoint - internet gateway, NAT device, VPN connection 또는 AWS Direct Connect connection없이, VPC에서 AWS service들과 VPC endpoint service들에 연결할 수 있도록 해준다. VPC에 있는 인스턴스들은 service에 있는 리소스들과 커뮤니케이션 하기 위해서 public IP address가 필요없다.
- CIDR block - Classless Inter-Domain Routing. 인터넷 프로토콜 주소 할당, route aggregation methodology.