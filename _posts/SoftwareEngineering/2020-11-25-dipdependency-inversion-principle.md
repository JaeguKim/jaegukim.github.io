---
layout: post
title: "[Inversion of Control 이해하기] Chapter 2 - DIP(Dependency Inversion Principle)"
date: 2020-11-25 20:58:00 +0900
categories: [SoftwareEngineering]
---

# **Dependency Inversion Principle**

## DIP의 정의

1. High-level 모듈들은 low-level 모듈들을 의존해서는 안된다. 둘다 Abstraction에 의존해야한다.

2. Abstraction들은 detail들에 의존해서는 안된다. Detail들은 abstraction들에 의존해야한다.

DIP를 이해하기 위해서 아래의 코드를 보자.
``` csharp
public class CustomerBusinessLogic
{
    public CustomerBusinessLogic()
    {
    }

    public string GetCustomerName(int id)
    {
        DataAccess _dataAccess = DataAccessFactory.GetDataAccessObj();

        return _dataAccess.GetCustomerName(id);
    }
}

public class DataAccessFactory
{
    public static DataAccess GetDataAccessObj() 
    {
        return new DataAccess();
    }
}

public class DataAccess
{
    public DataAccess()
    {
    }

    public string GetCustomerName(int id) {
        return "Dummy Customer Name"; // get it from DB in real app
    }
}
```

위의 예에서 보면, IoC를 달성하기 위해서 factory pattern을 사용하였다. 하지만 ```CustomerBusinessLogic``` class는 concrete ```DataAccess```를 사용하고 있으므로 여전히 tightly coupled 되어있다.

## Abstraction이란?

프로그래밍에서 abstraction이란 non-concrete한 interface나 abstract class를 만드는것을 말한다.

위에서 ```CustomerBusinessLogic```(high-level-module)은 ```DataAccess``` class(low-level module)에 의존해서는 안된다. 두 클래스모두 abstraction(interface, abstract class)에 의존해야만 한다.

이를 위해서 다음의 interface를 만든다.

``` csharp
public interface ICustomerDataAccess
{
    string GetCustomerName(int id);
}
```

그리고 ```ICustomerDataAccess```를 구현하는 ```CustomerDataAccess``` 클래스를 만든다.

``` csharp
public class CustomerDataAccess: ICustomerDataAccess
{
    public CustomerDataAccess()
    {
    }

    public string GetCustomerName(int id) {
        return "Dummy Customer Name";        
    }
}
```

그리고 factory class를 ```ICustomerDataAccess```를 리턴하도록 다음과같이 수정한다.

```csharp
public class DataAccessFactory
{
    public static ICustomerDataAccess GetCustomerDataAccessObj() 
    {
        return new CustomerDataAccess();
    }
}
```

마지막으로 ```CustomerBusinessLogic``` 클래스를 다음과 같이 수정한다.

``` csharp
public class CustomerBusinessLogic
{
    ICustomerDataAccess _custDataAccess;

    public CustomerBusinessLogic()
    {
        _custDataAccess = DataAccessFactory.GetCustomerDataAccessObj();
    }

    public string GetCustomerName(int id)
    {
        return _custDataAccess.GetCustomerName(id);
    }
}
```

결과적으로 
1. high-level-module(CustomerBusinessLogic)과 low-level module(CustomerDataAccess)는 abstraction(ICustomerDataAccess)에 의존한다. 

2. abstraction(ICustomerDataAccess)는 detail(CustomerDataAccess)에 의존하지 않는다, 반대로 detail은 abstraction에 의존한다.

완성된 DIP 예시는 아래와 같다.

``` csharp
public interface ICustomerDataAccess
{
    string GetCustomerName(int id);
}

public class CustomerDataAccess: ICustomerDataAccess
{
    public CustomerDataAccess() {
    }

    public string GetCustomerName(int id) {
        return "Dummy Customer Name";        
    }
}

public class DataAccessFactory
{
    public static ICustomerDataAccess GetCustomerDataAccessObj() 
    {
        return new CustomerDataAccess();
    }
}

public class CustomerBusinessLogic
{
    ICustomerDataAccess _custDataAccess;

    public CustomerBusinessLogic()
    {
        _custDataAccess = DataAccessFactory.GetCustomerDataAccessObj();
    }

    public string GetCustomerName(int id)
    {
        return _custDataAccess.GetCustomerName(id);
    }
}
```

결과적으로, 우리는 ```ICustomerDataAccess```를 구현하는 다른 클래스를 쉽게 사용할수 있게 되었다.

여전히, 완전한  loosely coupled 클래스는 달성하지 못하였다. 왜냐하면 ``` CustomerBusinessLogic``` 클래스가 ```ICustomerDataAccess```의 레퍼런스를 얻기위해서 여전히 factory class를 사용하고 있기 때문이다. 이 문제를 해결하는데 도움을 주는 패턴이 Dependency Injection Pattern이다. 다음 챕터에서는 Dependency Injection(DI)와 Strategy Pattern을 사용하는 법을 배워보자.

## 출처
[https://www.tutorialsteacher.com/ioc/dependency-inversion-principle](https://www.tutorialsteacher.com/ioc/dependency-inversion-principle)