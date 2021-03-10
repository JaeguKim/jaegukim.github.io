---
layout: post
title: "[Inversion of Control 이해하기] Chapter 3 - Dependency Injection"
date: 2020-11-25 21:00:00 +0900
categories: [SoftwareEngineering]
---

Dependency Injection(DI)는 IoC를 구현하기위해 사용되는 디자인 패턴이다. DI는 의존하는 객체들을 class 밖에서 생성하도록 허락하며, 그러한 객체들을 여러가지 방법을 통해서 class에 제공해준다.

Dependency Injection pattern은 3가지 유형의 클래스를 포함한다.

1. **Client Class**: The client class (dependent class)는 service class에 의존하는 클래스를 뜻한다.

2. **Service Class**: The service class(dependency)는 client class에 서비스를 제공하는 클래스를 뜻한다.

3. **Injector Class**: The Injector class는 client class에 service class 객체를 주입하는 클래스를 뜻한다.

다음은 위의 세클래스들간의 관계를 나타낸 그림이다.

![img](https://www.tutorialsteacher.com/Content/images/ioc/DI.png)

[source](https://www.tutorialsteacher.com/Content/images/ioc/DI.png)

위에서 보듯이, injector class는 service class의 객체를 생성하여 client 객체에게 주입하여준다.
DI pattern은 service class 객체 생성의 책임을 client class 밖으로 분리한다.

# Dependency Injection의 유형

- **Constructor Injection** : client class의 생성자를 통해서 의존성을 주입한다.

- **Property Injection** : Setter Injection이라고도 불리는데, client class의 public property를 통해서 의존성을 주입한다.

- **Method Injection** : client class는 dependency를 제공하기 위한 method를 선언하고 있는 interface를 구현하고 있고 injector는 client class에게 의존성을 제공하기 위해서 interface를 사용한다.

아래는 DIP 섹션에서 구현했던 코드이다.

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

위 코드에서 ```CustomerBusinessLogic``` 클래스 내부에서 ```DataAccessFactory```를 사용함을 알수있다. ```ICustomerDataAccess```의 또다른 구현을 사용하고 싶다고 가정하자. 이 경우에 ```CustomerBusinessLogic```의 소스코드를 변경해야함을 알수있다. 예를들어, ```DataAccessFactory.GetCustomerDataAccessObj()``` 대신 ```DataAccessFactory.GetEmployeeDataAccessObj()``` 로 변경하는 것처럼 말이다.
DI pattern은 위와같은 문제를 해결한다.

다음 그림은 위의 예시에 대한 DI Pattern 구현을 나타낸 그림이다.

![img](https://www.tutorialsteacher.com/Content/images/ioc/DI-example.png)

## Constructor Injection

생성자를 통해서 dependency를 제공하는것을 말한다.

예시코드를 보자.

``` csharp
public class CustomerBusinessLogic
{
    ICustomerDataAccess _dataAccess;

    public CustomerBusinessLogic(ICustomerDataAccess custDataAccess)
    {
        _dataAccess = custDataAccess;
    }

    public CustomerBusinessLogic()
    {
        _dataAccess = new CustomerDataAccess();
    }

    public string ProcessCustomerData(int id)
    {
        return _dataAccess.GetCustomerName(id);
    }
}

public interface ICustomerDataAccess
{
    string GetCustomerName(int id);
}

public class CustomerDataAccess: ICustomerDataAccess
{
    public CustomerDataAccess()
    {
    }

    public string GetCustomerName(int id) 
    {
        //get the customer name from the db in real application        
        return "Dummy Customer Name"; 
    }
}
```

위 예시에서 ```CustomerBusinessLogic```은 ```ICustomerDataAccessConstructor```타입의 파라미터를 가진 생성자를 포함하고 있다. 
이제 호출 class에서 ```ICustomerDataAccess```에 대한 객체를 주입해야한다.

``` csharp
public class CustomerService
{
    CustomerBusinessLogic _customerBL;

    public CustomerService()
    {
        _customerBL = new CustomerBusinessLogic(new CustomerDataAccess());
    }

    public string GetCustomerName(int id) {
        return _customerBL.ProcessCustomerData(id);
    }
}
```

위 코드에서 보듯이 ```CustomerService``` 클래스가 ```CustomerDataAccess``` 객체를 생성하여 ```CustomerBusinessLogic```클래스에 주입하는것을 알수있다. 따라서 ```CustomerBusinessLogic```는 더이상 ```CustomerDataAccess``` 객체를 ```new```키워드 또는 factory 클래스를 통해서 생성할 필요가 없게 되었다. 결과적으로 ```CustomerBusinessLogic```과 ```CustomerDataAccess```간에 결합도가 낮아졌다.

## Property Injection

Property Injection에서는 public property를 통해서 의존성이 제공된다.

``` csharp
public class CustomerBusinessLogic
{
    public CustomerBusinessLogic()
    {
    }

    public string GetCustomerName(int id)
    {
        return DataAccess.GetCustomerName(id);
    }

    public ICustomerDataAccess DataAccess { get; set; }
}

public class CustomerService
{
    CustomerBusinessLogic _customerBL;

    public CustomerService()
    {
        _customerBL = new CustomerBusinessLogic();
        _customerBL.DataAccess = new CustomerDataAccess();
    }

    public string GetCustomerName(int id) {
        return _customerBL.GetCustomerName(id);
    }
}
```

위에서 보듯이, ```CustomerBusinessLogic``` 클래스는 ```DataAccess```라는 public property를 가지고 있고 ```CustomerService``` 클래스는 ```CustomerDataAccess``` 클래스를 생성하여 public property에 할당해준다.

## Method Injection

method injection에서는 의존성들이 함수를 통해서 주입된다. 이 메소드는 class method 일수도 있고 interface method 일수도 있다.

다음 코드는 interface method를 이용해서 method injection을 구현한 예이다.

``` csharp
interface IDataAccessDependency
{
    void SetDependency(ICustomerDataAccess customerDataAccess);
}

public class CustomerBusinessLogic : IDataAccessDependency
{
    ICustomerDataAccess _dataAccess;

    public CustomerBusinessLogic()
    {
    }

    public string GetCustomerName(int id)
    {
        return _dataAccess.GetCustomerName(id);
    }
        
    public void SetDependency(ICustomerDataAccess customerDataAccess)
    {
        _dataAccess = customerDataAccess;
    }
}

public class CustomerService
{
    CustomerBusinessLogic _customerBL;

    public CustomerService()
    {
        _customerBL = new CustomerBusinessLogic();
        ((IDataAccessDependency)_customerBL).SetDependency(new CustomerDataAccess());
    }

    public string GetCustomerName(int id) {
        return _customerBL.GetCustomerName(id);
    }
}
```

위 예에서 보듯이, ```CustomerBusinessLogic```는 ```IDataAccessDependency```를 구현하고 있고 interface는 ```SetDependency()```함수를 포함한다. injector class ```CustomerService```
는 이 함수를 dependent class(CustomerDataAccess)를 client class에 주입하기 위해서 사용한다.

지금까지, loosely coupled class들을 구현하기위해 IoC, DIP 그리고 DI를 적용했다. 실제 프로젝트에서는 dependent class들이 많아서 이러한 패턴을 구현하는데는 시간이 많이 소요된다. 바로 이문제를 해결하기 위해서 **IoC Container**가 도움을 줄 수 있다.
다음 챕터에서는 IoC Container에 대해서 알아보자.

## 출처
[https://www.tutorialsteacher.com/ioc/dependency-injection](https://www.tutorialsteacher.com/ioc/dependency-injection)