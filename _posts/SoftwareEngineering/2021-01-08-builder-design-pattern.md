---
layout: post
title: "Builder Design Pattern"
date: 2021-01-08 22:04:00 +0900
categories: [SoftwareEngineering]
---

## Builder Design Pattern

상대적으로 복잡한 객체생성을 다루는 패턴중 하나
또다른 객체를 사용하여 객체를 생성하기 위한 객체화 과정을 분리

## Example

``` java
public class BankAccount {
    
    private String name;
    private String accountNumber;
    private String email;
    private boolean newsletter;

    // constructors/getters
    
    public static class BankAccountBuilder {
        // builder code
    }
}
```

``` java
public static class BankAccountBuilder {
    
    private String name;
    private String accountNumber;
    private String email;
    private boolean newsletter;
    
    public BankAccountBuilder(String name, String accountNumber) {
        this.name = name;
        this.accountNumber = accountNumber;
    }

    public BankAccountBuilder withEmail(String email) {
        this.email = email;
        return this;
    }

    public BankAccountBuilder wantNewsletter(boolean newsletter) {
        this.newsletter = newsletter;
        return this;
    }
    
    public BankAccount build() {
        return new BankAccount(this);
    }
}
```

``` java
BankAccount newAccount = new BankAccount
  .BankAccountBuilder("Jon", "22738022275")
  .withEmail("jon@example.com")
  .wantNewsletter(true)
  .build();
```

## 언제 Builder pattern을 사용할 것인가?

1. 객체를 생성하는 과정이 매우 복잡할경우 (필수.옵션 파라미터들이 너무 많을경우)

2. 생성자 파라미터의 수의 증가가 생성자 리스트수도 증가시킬 경우

## 출처
[https://www.baeldung.com/creational-design-patterns#builder](https://www.baeldung.com/creational-design-patterns#builder)
