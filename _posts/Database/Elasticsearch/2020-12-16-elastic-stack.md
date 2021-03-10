---
layout: post
title: "Elastic Stack"
date: 2020-12-16 11:07:00 +0900
categories: [Database,Elasticsearch]
---

## Elastic Stack
- KIBANA
- BEATS
- LOGSTASH
- X-PACK
- ELASTICSEARCH

## Kibana
- analytics & visualization platform

- elastic search 데시보드, pie chart, line chart등을 생성가능

- 실시간 웹사이트 트래픽 모니터링 가능

- 이상 현상 감지, 데이터 예측 가능

- es의 웹 인터페이스

## Logstash

- 원래는 log를 처리하고 es에 보내는 용도로 사용됨

- 최근에는 기능이 확장되어 데이터 프로세싱 용도로 사용됨

- log stash pipeline은 input,filter,output으로 구성

- horizontally scalable

## X-Pack

- es & Kibana에게 추가적인 feature 추가

- Security : authentication 과  authorization을 es와 kibana에게 제공

- Monitoring : es가 어떻게 돌고있는지에 대한 insight를 얻을수 있음. 

- Alerting : 이상현상이 발생했을때 알림기능 제공

- Reporting : 보고서를 자동으로 생성 및 이메일로 전송하는 기능제공

- Machine Learning : es와 Kibana에게 machine learning이 가능하게 함.

- Elasticsearch SQL : SQL로 es에 쿼리

## Beats

- Data Shippers

- 여러 종류의 데이터를 수집하고 es 또는 Logstash에 저장

## Elastic Stack

- ElasticSearch

- Kibana

- Logstash

- Beats

## ELK

- ElasticSearch

- Kibana

- Logstash