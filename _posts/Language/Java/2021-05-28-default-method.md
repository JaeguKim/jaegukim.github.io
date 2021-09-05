---
layout: post
title: "Default Method"
date: 2021-05-28 14:17:00 +0900
categories: [Language,Java]
---

Java에서는 인터페이스에 디폴트 메소드를 정의할 수 있다. 
먼저, 다음과 같은 인터페이스가 있다고 가정하자.

``` java
public interface TimeClient {
    void setTime(int hour, int minute, int second);
    void setDate(int day, int month, int year);
    void setDateAndTime(int day, int month, int year, int hour, int minute, int second);
    LocalDateTime getLocalDateTime();
}
```
그리고 위 인터페이스를 구현하는 다음의 클래스가 있다.

``` java
public class SimpleTimeClient implements TimeClient {

    private LocalDateTime dateAndTime;

    public SimpleTimeClient() {
        dateAndTime = LocalDateTime.now();
    }

    @Override
    public void setTime(int hour, int minute, int second) {
        LocalDate currentDate = LocalDate.from(dateAndTime);
        LocalTime timeToSet = LocalTime.of(hour, minute, second);
        dateAndTime = LocalDateTime.of(currentDate,timeToSet);
    }

    @Override
    public void setDate(int day, int month, int year) {
        LocalDate dateToSet = LocalDate.of(day,month,year);
        LocalTime currentTime = LocalTime.from(dateAndTime);
        dateAndTime = LocalDateTime.of(dateToSet,currentTime);
    }

    @Override
    public void setDateAndTime(int day, int month, int year, int hour, int minute, int second) {
        LocalDate dateToSet = LocalDate.of(day,month,year);
        LocalTime timeToSet = LocalTime.of(hour,minute,second);
        dateAndTime = LocalDateTime.of(dateToSet,timeToSet);
    }

    @Override
    public LocalDateTime getLocalDateTime() {
        return dateAndTime;
    }

    public String toString() {
        return dateAndTime.toString();
    }

    public static void main(String[] args) {
        TimeClient myTimeClient = new SimpleTimeClient();
        System.out.println(myTimeClient.toString());
    }
}
```

만약 인터페이스를 다음과 같이 수정한다면 어떻게 될까?

``` java
public interface TimeClient {
    void setTime(int hour, int minute, int second);
    void setDate(int day, int month, int year);
    void setDateAndTime(int day, int month, int year, int hour, int minute, int second);
    LocalDateTime getLocalDateTime();
    ZonedDateTime getZonedDateTime(String zoneString);
}
```

위와 같은 경우, 구현 클래스에서 추가된 함수를 구현해야 할 것이다. 하지만 디폴트 메소드를 구현하면 그럴필요가 없어진다.

``` java
public interface TimeClient {
    void setTime(int hour, int minute, int second);
    void setDate(int day, int month, int year);
    void setDateAndTime(int day, int month, int year, int hour, int minute, int second);
    LocalDateTime getLocalDateTime();

    static ZoneId getZoneId (String zoneString) {
        try {
            return ZoneId.of(zoneString);
        } catch (DateTimeException e) {
            System.err.println("Invalid time zone: " + zoneString +
                    "; using default time zone instead.");
            return ZoneId.systemDefault();
        }
    }

    default ZonedDateTime getZonedDateTime(String zoneString) {
        return ZonedDateTime.of(getLocalDateTime(), getZoneId(zoneString));
    }
}
```

위와 같이 정의하면, 하위 클래스에서는 새로운 함수를 구현할 필요가 없다. 언젠가는 유용한 특징인것같다.

## [출처](https://docs.oracle.com/javase/tutorial/java/IandI/defaultmethods.html)
