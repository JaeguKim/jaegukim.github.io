---
layout: post
title: "VPCs and subnets"
date: 2021-07-22 16:08:00 +0900
categories: [AWS]
---

VPC는 AWS 계정에 할당된 virtual network이다. AWS Cloud에서 다른 virtual network와 논리적으로 고립되어있다. AWS 자원들을 VPC에서 실행할 수 있게 된다.

VPC를 생성할때, IPv4 주소들을 Classless Inter-Domain Routing(CIDR) block으로 명시해주어야한다. 예를들면, 10.0.0.0/16과 같이 정의된다. 

다음 다이어그램은 IPv4 CIDR block을 가진 새로운 VPC를 보여준다.

![ 				VPC with the main route table 			](https://docs.aws.amazon.com/vpc/latest/userguide/images/vpc-diagram.png)

main route table은 다음과 같은 라우트를 가진다.

| Destination | Target |
| :---------- | :----- |
| 10.0.0.0/16 | local  |

VPC는 Region에있는 이용가능한 Zone에 걸쳐서 존재한다. VPC를 생성하고나서, 한개이상의 subnet을 각각의 Availability Zone에 추가할 수 있다. 필요에 따라 컴퓨팅, 스토리지, 데이터베이스 및 기타 선택 서비스를 최종 사용자에게 더 가깝게 배치하는 AWS 인프라 배포인 로컬 영역에 서브넷을 추가할 수 있다. Local Zone은 end user가 한 자릿수 millisecond 지연시간만에 실행할 수 있도록 허락한다. 각각의 subnet은 한가지 availability zone에서 존재해야 하고 여러 zone에 걸쳐서 존재할 수 없다. Availability Zone들은 다른 Availability Zone에서의 실패와는 단절되어있도록 설계된 distinct location이다. 도립된 Availability Zone에서 인스턴스를 실행함으로써, 단일 위치의 실패로부터 어플리케이션을 안전하게 보호할 수 있다. 각각의 subnet에 unique id가 부여된다.

또한 선택적으로 IPv6 CIDR block을 VPC에 적용할 수 있고 IPv6 CIDR 블락들을 subnet에 적용할 수도있다.

다음의 다이어그램은 여러 Availability Zones에 있는 Subnet으로 설정된 VPC를 보여준다. 1A,2A,3A는 VPC에 있는 인스턴스들이다. IPv6 CIDR block은 VPC와 연관되어있고 어떤 IPv6 CIDR 블락은 subnet 1과 연관있다. 인터넷 게이트웨이는 인터넷을 통해서 커뮤니케이션 될수 있도록 허용하고 VPN 연결은 corporate network와의 커뮤니케이션을 가능하게 한다.

![ 				VPC with multiple Availability Zones 			](https://docs.aws.amazon.com/vpc/latest/userguide/images/subnets-diagram.png)

만약 subnet traffic이 인터넷 게이트웨이로 라우팅 되면, 서브넷은 public subnet이라고 알려진다. 이 다이어그램에서 subnet 1은 public subnet이다. 만약 public subnet에 있는 인스턴스가 IPv4를 통해서 커뮤니케이션 되어야한다고 한다면, IPv4 주소 또는  Elastic IP address(IPv4)를 가져야 한다. 만약 public subnet에 있는 인스턴스가 IPv6를 통해서 커뮤니케이션 되어야 한다면, IPv6를 가져야 한다.

만약 subnet이 internet gateway로 가는 라우트가 없다면, subnet은  private subnet이라고 불린다. 위 다이어그램에서 subnet 2가 private subnet이다. 

만약 subnet이 인터넷 게이트웨이에 대한 route가 없지만 virtual private gateway로 라우트된 트래픽이 있을 경우 (Site-to-Site VPN connection을 위해서), subnet은 VPN-only subnet이라고 불린다. 이 다이어그램에서 subnet 3가 VPN-only subnet이다. 현재 Site-to-Site VPN connection 을 위한 IPv6 트래픽은 지원하지 않는다.

계정마다 VPC와 Subnet에 대한 할당량이 있다.

### VPC and subnet sizing

Amazon VPC는 IPv4와 IPv6 addressing을 지원하고 각자마다 다른 CIDR block size 할당량이 있다. 기본적으로 모든 VPC와 Subnet들은 IPv4 CIDR 블락들을 가져야 한다 - 이 행동은 바꿀수가 없다.

선택적으로 IPv6 CIDR 블락은 VPC와 연관시킬 수 있다.

### VPC and Subnet Sizing for IPv4

VPC를 생성할때, VPC에 대한 IPv4 CIDR 블락을 명시해야 한다. 허용된 블락 사이즈는 /16 netmask(65,536 IP addresses)와 /28 netmasks(16 addresses) 사이다. VPC를 생성하고 나서, Secondary CIDR 블락들을 VPC와 연관시킬 수 있다.

VPC를 생성할때, private IPv4 address 범위로 부터 CIDR 블락을 명시하는것을 추천한다.

| RFC 1918 range                                        | Example CIDR block                                           |
| :---------------------------------------------------- | :----------------------------------------------------------- |
| `10.0.0.0` - `10.255.255.255` (10/8 prefix)           | Your VPC must be /16 or smaller, for example, `10.0.0.0/16`. |
| `172.16.0.0` - `172.31.255.255` (172.16/12 prefix)    | Your VPC must be /16 or smaller, for example, `172.31.0.0/16`. |
| `192.168.0.0` - `192.168.255.255` (192.168/16 prefix) | Your VPC can be smaller, for example `192.168.0.0/20`.       |


