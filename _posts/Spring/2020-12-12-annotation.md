---
layout: post
title: "annotation"
date: 2020-12-12 23:09:00 +0900
categories: [Spring]
---

## @Configuration

 해당 클래스에서 1개이상의 Bean을 생성하고 있음을 명시 @Bean 어노테이션을 사용하는 클래스의 경우 반드시 @Configuration과 함께 사용해주어야 함.
만약 그렇지않으면, 생성된 객체가 싱글톤을 보장받지 못한다.

## @Component

**직접 개발한 클래스**를 Bean으로 등록하고자 하는 경우에 사용
@Target이 TYPE로 지정되어 Class위에서만 선언될수 있다.

## @ContextConfiguration

**integration test**를 위해, ApplicationContext를 어떻게 load하고 configure할것인지 결정하기위해서 사용되는 class-level metadata를 정의한다.

## @Import

다수의 configuration class들을 control해야하는 상황에서, 모든 configuration class를 Import 어노테이션에 명시할수는 없다. 그러므로 여러 configuration class를 하나로 묶어서 표현하는 방법이 필요하다.
@Component또한 포함할수있다.

(예시)
Before

``` java
@ExtendWith(SpringExtension.class)
@ContextConfiguration(classes = { BirdConfig.class, CatConfig.class, DogConfig.class })
class ConfigUnitTest {

    @Autowired
    ApplicationContext context;

    @Test
    void givenImportedBeans_whenGettingEach_shallFindIt() {
        assertThatBeanExists("dog", Dog.class);
        assertThatBeanExists("cat", Cat.class);
        assertThatBeanExists("bird", Bird.class);
    }

    private void assertThatBeanExists(String beanName, Class<?> beanClass) {
        Assertions.assertTrue(context.containsBean(beanName));
        Assertions.assertNotNull(context.getBean(beanClass));
    }
}
```

After

``` java
@Configuration
@Import({ DogConfig.class, CatConfig.class })
class MammalConfiguration {
}
```
``` java
@ExtendWith(SpringExtension.class)
@ContextConfiguration(classes = { MammalConfiguration.class })
class ConfigUnitTest {

    @Autowired
    ApplicationContext context;

    @Test
    void givenImportedBeans_whenGettingEach_shallFindOnlyTheImportedBeans() {
        assertThatBeanExists("dog", Dog.class);
        assertThatBeanExists("cat", Cat.class);

        Assertions.assertFalse(context.containsBean("bird"));
    }

    private void assertThatBeanExists(String beanName, Class<?> beanClass) {
        Assertions.assertTrue(context.containsBean(beanName));
        Assertions.assertNotNull(context.getBean(beanClass));
    }
}
```

그리고 다음과 같이 묶어서 표현할수도 있다.
``` java
@Configuration
@Import({ MammalConfiguration.class, BirdConfig.class })
class AnimalConfiguration {
}
```

``` java
@ExtendWith(SpringExtension.class)
@ContextConfiguration(classes = { AnimalConfiguration.class })
class AnimalConfigUnitTest {
    // same test validating that all beans are available in the context
}
```

## @ComponentScan vs @Import

@ComponentScan은 주로 기본적으로 포함할 베이스 패키지에 대하여 컴포넌트 탐색을 수행하고, @Import는 추가적으로 추가할 컴포넌트나 configuration을 추가할때 사용한다.

## @Target
선언된 타입이 적용가능한 범위를 명시

## @Retention
어느 시점까지 어노테이션의 메모리를 가져갈지 설정

- SOURCE : 어노테이션을 사실상 comment로 사용, 컴파일러가 컴파일할때 해당 어노테이션의 메모리를 버림

- CLASS : 컴파일러가 컴파일에서는 어노테이션의 메모리를 가져가지만 런타임시에는 사라짐. 

- RUNTIME : 어노테이션을 런타임시까지 사용가능. JVM이 자바바이트코드가 담긴 class파일에서 런타임환경을 구성하고 런타임을 종료할때까지 메모리는 살아있음.

## @DependsOn

정의된 Bean이 현재 Bean이 초기화되기 전에 초기화될수 있도록 보장

예를들면 FileProcessor는 FileReader와 FileWriter가 초기화 되고 나서 초기화 되어야한다.

``` java
@Configuration
@ComponentScan("com.baeldung.dependson")
public class Config {
 
    @Bean
    @DependsOn({"fileReader","fileWriter"})
    public FileProcessor fileProcessor(){
        return new FileProcessor();
    }
    
    @Bean("fileReader")
    public FileReader fileReader() {
        return new FileReader();
    }
    
    @Bean("fileWriter")
    public FileWriter fileWriter() {
        return new FileWriter();
    }   
}
```

## @Inherited 
annotated classes의 sub classes들이 super class의 annotation과 같은 annotation을 갖게된다.

예시는 다음과 같다.
``` java
@Inherited
@Target(ElementType.TYPE)
@Retention(RetentionPolicy.RUNTIME)
public @interface InheritedAnnotationType {
    
}

@Target(ElementType.TYPE)
@Retention(RetentionPolicy.RUNTIME)
public @interface UninheritedAnnotationType {
    
}
```

만약 세개의 클래스가 다음과 같이 annotated 되어있으면

``` java
@UninheritedAnnotationType
class A {
    
}

@InheritedAnnotationType
class B extends A {
    
}

class C extends B {
    
}
```
다음과 같이 실행해보면 결과는 아래와같다.

``` java
System.out.println(new A().getClass().getAnnotation(InheritedAnnotationType.class));
System.out.println(new B().getClass().getAnnotation(InheritedAnnotationType.class));
System.out.println(new C().getClass().getAnnotation(InheritedAnnotationType.class));
System.out.println("_________________________________");
System.out.println(new A().getClass().getAnnotation(UninheritedAnnotationType.class));
System.out.println(new B().getClass().getAnnotation(UninheritedAnnotationType.class));
System.out.println(new C().getClass().getAnnotation(UninheritedAnnotationType.class));
```

```
null
@InheritedAnnotationType()
@InheritedAnnotationType()
_________________________________
@UninheritedAnnotationType()
null
null
```

## @Documented

javadoc으로 api문서를 만들때 어노테이션에 대한 설명도 포함하도록 지정해줌.

## @Autowired

@Autowired는 default로 required = true로 세팅되어있음.
- required = true : annotated dependency가 필요함을 의미
- required = false : annotated dependency가 필수는 아님을 의미

## @RequiredArgsConstructor

이 어노테이션은 초기화 되지않은 final 필드나, @NonNull 이 붙은 필드에 대해 생성자를 생성해 줍니다.

## @Component vs @Repository vs @Service vs @Controller

| Annotation | Meaning 
| --- | ---
| @Component | generic stereotype for Spring-managed component
| @Repository | stereotype for persistence layer
| @Service | stereotype for service layer

