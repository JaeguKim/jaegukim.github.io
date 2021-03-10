---
layout: post
title: "[Inversion of Control 이해하기] Chapter 1 - Inversion of Control의 정의와 예시"
date: 2020-11-25 20:54:00 +0900
categories: [SoftwareEngineering]
---

# Overview

![img](https://www.tutorialsteacher.com/Content/images/ioc/principles-and-patterns.png)

[출처](https://www.tutorialsteacher.com/Content/images/ioc/principles-and-patterns.png)

위 그림에서 보듯이 IoC와 DIP는 class들을 디자인할때 사용되어야 하는 high level design principle들이다. principle이기 때문에 best practice를 추천해주긴 하지만 구체적인 구현사항을 제공하지는 않는다. DI는 pattern이고 IoC container는 framework이다.

# Inversion of Control

IoC는 클래스들 사이에 느슨한 커플링(loose coupling)을 달성하기 위해서 여러종류의 control을 뒤집는 것을 추천하는 **principle**이다.

여기서 control이란 클래스가 갖고있는 부가적인 책임들을 말하는데, 예를들면 application의 흐름, 객체 생성, 의존 객체 생성 및 바인딩을 말한다.

비유로 설명하면, 차를 운전해서 회사로 간다고 가정해보자. 이때 우리는 차를 control해서 회사로 간다. 하지만 만약 택시를 불러서 택시기사로 하여금 회사로 가도록 맡긴다면 이는 제어의 역전(Inversion of Control)로 볼수있다.

## Control Over the Flow of a Program
아래와 같이 Main함수에서 프로그램의 흐름을 control하는 경우를 보자.

``` csharp
namespace FlowControlDemo
{
    class Program
    {
        static void Main(string[] args)
        {
           bool continueExecution = true;
            do
            {
                Console.Write("Enter First Name:");
                var firstName = Console.ReadLine();

                Console.Write("Enter Last Name:");
                var lastName = Console.ReadLine();

                Console.Write("Do you want to save it? Y/N: ");

                var wantToSave = Console.ReadLine();

                if (wantToSave.ToUpper() == "Y")
                    SaveToDB(firstName, lastName);

                Console.Write("Do you want to exit? Y/N: ");

                var wantToExit = Console.ReadLine();

                if (wantToExit.ToUpper() == "Y")
                    continueExecution = false;

            }while (continueExecution);
         
        }

        private static void SaveToDB(string firstName, string lastName)
        {
            //save firstName and lastName to the database here..
        }
    }
}
```

위 프로그램은 인풋을 받아서 데이터를 저장하는 과정을 반복하고 실행흐름이 Main() 함수에 의해서 control되고 있다.

GUI-based application을 이용하면 IoC를 달성할수 있다. 프레임워크가 이벤트들을 통해서 프로그램의 흐름을 통제하기 때문이다.

![img](https://www.tutorialsteacher.com/Content/images/ioc/winform.png)

[출처](https://www.tutorialsteacher.com/Content/images/ioc/winform.png)

## Control Over the Dependent Object Creation

IoC는 또한 dependent class에 대한 객체들을 생성할때도 적용된다. 
다음 코드를 보자.

``` csharp
public class A
{
    B b;

    public A()
    {
        b = new B();
    }

    public void Task1() {
        // do something here..
        b.SomeMethod();
        // do something here..
    }

}

public class B {

    public void SomeMethod() { 
        //doing something..
    }
}
```

위 코드에서 보면, class A는 Task1에서 b.someMethod() 함수를 호출한다. 따라서 class A는 class B에 의존한다.
그리고 class A는 class B의 생성을 통제하고 있다.

IoC를 이용해서 제어를 역전시켜보자. 즉, 다른 클래스에 제어를 맡겨보자. 

``` csharp
public class A
{
    B b;

    public A()
    {
        b = Factory.GetObjectOfB ();
    }

    public void Task1() {
        // do something here..
        b.SomeMethod();
        // do something here..
    }
}

public class Factory
{
    public static B GetObjectOfB() 
    {
        return new B();
    }
}
```

위에서 보듯이 class A의 생성을 Factory 클래스가 담당하는 것을 알수있다.

다음과 같은 패턴이 IoC principle을 구현한다.

![img](https://www.tutorialsteacher.com/Content/images/ioc/ioc-patterns.png)
[출처](https://www.tutorialsteacher.com/Content/images/ioc/ioc-patterns.png)

## 출처
[https://www.tutorialsteacher.com/ioc/inversion-of-control](https://www.tutorialsteacher.com/ioc/inversion-of-control)