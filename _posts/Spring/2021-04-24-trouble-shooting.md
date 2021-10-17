---
layout: post
title: "Trouble Shooting(Spring)"
date: 2021-04-24 15:19:00 +0900
categories: [Spring]
---

## Your ApplicationContext is unlikely to start due to a @ComponentScan of the default package.

> Main Application 파일을 java 폴더 바로 밑에 두어서 생기는 문제이다.  

## com.fasterxml.jackson.databind.exc.InvalidDefinitionException: Cannot construct instance

``` java
@Getter
@Setter
@Builder
@AllArgsConstructor
public class PeopleInfo {
    private int id;
    private int numberOfCurrentPeople;
    private int numberOfNewPeople;
    private String time;
}
```

``` java
public class PeopleInfoDeserializer implements Deserializer<PeopleInfo> {
    @Override
    public PeopleInfo deserialize(String topic, byte[] data) {
        ObjectMapper mapper = new ObjectMapper();
        PeopleInfo peopleInfo = null;
        try {
            peopleInfo = mapper.readValue(data,PeopleInfo.class);
        } catch (Exception e) {
            e.printStackTrace();
        }
        return peopleInfo;
    }
}
```

위와 같이 정의해 두었을때, byte 배열을 ```PeopleInfo```로 deserialize할때 발생한 에러이다. 해결책은 ```PeopleInfo```에 아래와 같이 Default 생성자를 선언해놓으면 된다.

``` java
@Getter
@Setter
@Builder
@AllArgsConstructor
@NoArgsConstructor // 추가!
public class PeopleInfo {
    private int id;
    private int numberOfCurrentPeople;
    private int numberOfNewPeople;
    private String time;
}
```
