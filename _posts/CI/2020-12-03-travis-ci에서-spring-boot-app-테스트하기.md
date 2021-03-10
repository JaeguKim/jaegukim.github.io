---
layout: post
title: "Travis CI에서 Spring boot app 테스트하기"
date: 2020-12-03 14:03:00 +0900
categories: [CI]
---

Spring Boot 앱을 CI를 통해서 테스트를 하고 도커로 배포하기 하려는 과정중에 테스트가 실패하는 현상이 발생했다.
이유는 Spring Boot 앱의 테스트 코드가 배포환경의 Database에 의존했기 때문이었다.

이 문제들 다음과 같이 해결하였다.

# 1. Mockito를 이용해서 각각의 layer들을 독립적으로 테스트하도록 리펙토링

처음 시도한 방법은 service 와 rest controller에서 의존하고있는 객체들을 Mockito를 이용해서 mocking하는 방법으로 변경하였다. 

다음은 UserService를 Mockito를 이용하여 작성한 테스트 코드의 일부분이다.

``` java
	@Autowired private UserService userService;
	
	@MockBean(UserRepository.class) 
	private UserRepository userRepository;
	
	@Test
	public void findAllTest() {
		User user1 = new User("jaegu","kim","jaegu88@gmail.com","1234");
		User user2 = new User("junhyun","park","junhyun@gmail.com","1234");
		Mockito.when(userRepository.findAll()).thenReturn(Arrays.asList(user1,user2));
		List<User> resultList = userService.findAll();
		assertTrue(resultList.size()>=2);
	}
```

위와 같이 UserRepository를 실제로 의존하지 않고 UserRepository의 동작을 가정할수 있기 때문에 해당 service를 독립적으로 테스트 할수 있다.

다음은 UserRestController를 Mockito를 사용하여 작성한 테스트 코드의 일부이다.

``` java
	@Test
	public void findAllTest() throws Exception {
		User user1 = new User("jaegu","kim","jaegu88@gmail.com","1234");
		User user2 = new User("junhyun","park","junhyun@gmail.com","1234");
		Mockito.when(userService.findAll()).thenReturn(Arrays.asList(user1,user2));
	
		String uri = "/api/users";
		MvcResult mvcResult = mvc.perform(MockMvcRequestBuilders.get(uri)
				.accept(MediaType.APPLICATION_JSON_VALUE)).andReturn();

		int status = mvcResult.getResponse().getStatus();
		assertEquals(200, status);
		
		ObjectMapper mapper = new ObjectMapper();
		List<User> result = mapper.readValue(mvcResult.getResponse().getContentAsString(), new TypeReference<List<User>>() {});
		assertEquals(2,result.size());
	}
```

위코드에서 보듯이 UserService에 의존하지 않고 동작을 가정하므로써 UserRestController를 테스트 할수 있다.

위의 과정을 커지고 테스트를 했지만 다음과 같은 에러가 발생하였다.

```
    java.lang.IllegalStateException at DefaultCacheAwareContextLoaderDelegate.java:132
        Caused by: org.springframework.beans.factory.BeanCreationException at BeanDefinitionValueResolver.java:342
            Caused by: org.springframework.beans.factory.BeanCreationException at AbstractAutowireCapableBeanFactory.java:1794
                Caused by: org.hibernate.service.spi.ServiceException at AbstractServiceRegistryImpl.java:275
                    Caused by: org.hibernate.HibernateException at DialectFactoryImpl.java:100
```

# 2. 테스트용 Embedded DB를 세팅

위의 에러는 ci에서 빌드할때 사용하는 application.yml 파일이 여전히 실제 데이터베이스에 의존하고 있기 때문이다. 이를 위해서 test용 application.yml을 참조하도록 수정했다. 하지만 이번에는 다음과 같은 에러가 발생했다.

```
    java.lang.IllegalStateException at DefaultCacheAwareContextLoaderDelegate.java:132
        Caused by: org.springframework.beans.factory.UnsatisfiedDependencyException at ConstructorResolver.java:797
            Caused by: org.springframework.beans.factory.BeanCreationException at ConstructorResolver.java:655
                Caused by: org.springframework.beans.BeanInstantiationException at SimpleInstantiationStrategy.java:185
                    Caused by: org.springframework.boot.autoconfigure.jdbc.DataSourceProperties$DataSourceBeanCreationException at DataSourceProperties.java:234
```

위 에러는 data source가 세팅되어있지 않아서 생겨난 문제였고, build.gradle 파일에 embedded db를 설정하므로써 해결하였다.

```
    testCompile group: 'com.h2database', name: 'h2', version: '1.4.197'
```

testCompile로 정의하여 테스트를 위해서만 h2database dependency group를 사용하도록 했다.

# 결과
결과적으로 Travis CI에서는 다음의 커멘드로 spring boot 앱을 테스트하게 된다.

```
./gradlew clean build -Pprofile=test && ./gradlew clean build -Pprofile=ci -x test && docker build --tag kimwithglasses/safe-place-api:0.0.1
```

처음에는 test용 프로파일로 테스트를 수행하고, ci 프로파일로 배포를 하게되는 방식이다.



