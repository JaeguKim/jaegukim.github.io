---
layout: post
title: "MAC address, IP address"
date: 2017-07-17
categories: [Network]
---
# MAC Address
- MAC 주소는 일반적으로 제조업체의 등록된 식별 번호로 인코딩되며 이를 BIA(burned-in address)로 부를 수 있다. 또, 이더넷 하드웨어 주소(Ethernet hardware address, EHA), 하드웨어 주소, 물리 주소(메모리 물리 주소와 다름)로 부르기도 한다

- IP Address
인터넷상에서 라우팅을 효율적으로 하기 위하여 물리적인 네트웍 주소와 일치하는 개념으로 부여된 32 비트의 주소가 IP 주소

- IP Address가 MAC address에 비해 가지는 장점
같은 네트워크 상에 있는지 그렇지 않은지 판단가능
mac address는 물리연결만 가능하게 하지만 ip address는 Host or Network interface Identification and Location addressing을 지원한다.

# 라우터는 어떻게 IP주소를 보고 MAC주소를 찾아낼 것인가?
바로 ARP(Address Resoulation Protocol)이다.
ARP는 IP주소를 가지고 MAC주소를 찾아가는 프로토콜이다.
