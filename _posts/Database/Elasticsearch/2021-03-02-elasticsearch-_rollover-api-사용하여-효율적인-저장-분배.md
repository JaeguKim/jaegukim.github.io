---
layout: post
title: "Elasticsearch _rollover API 사용하여, 효율적인 저장 분배"
date: 2021-03-02 16:47:00 +0900
categories: [Database,Elasticsearch]
---

## Elasticsearch _rollover API 사용하여, 효율적인 저장 분배

### Skew란?

데이터가 전체 샤드에 골고루 분배되지 않는 상황

![img](https://d2908q01vomqb2.cloudfront.net/ca3512f4dfa95a03169c5a670a4c91a19b3077b4/2019/08/06/Rollover3.jpg)

### Rollover를 사용하여 해결하기

[_rollover API](https://www.elastic.co/guide/en/elasticsearch/reference/7.0/indices-rollover-index.html)는  임계치를 넘어가면 새로운 인덱스를 생성한다.

```json
POST _aliases
{
  "actions": [
    {
      "add": {
        "index": "weblogs-000001",
        "alias": "weblogs",
        "is_write_index": true
      }
    }
  ]
}
```

위 작업을 cron, 스케줄링 도구로 실행할수 있다.

```json
POST /weblogs/_rollover 
{
  "conditions": {
    "max_size":  "10gb"
  }
}
```

rollover 조건은 위와 같이 설정할수 있다.



## [출처](https://aws.amazon.com/blogs/opensource/open-distro-for-elasticsearch-rollover-storage-best-practice/)


