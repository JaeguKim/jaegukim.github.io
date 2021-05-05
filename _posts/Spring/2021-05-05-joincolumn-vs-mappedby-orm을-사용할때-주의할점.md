---
layout: post
title: "JoinColumn vs MappedBy (ORM을 사용할때 주의할점)"
date: 2021-05-05 20:58:00 +0900
categories: [Spring]
---

## JPA JoinColumn vs mappedBy

### Unidirectional one-to-many association

```@OneToMany``` 와 ```@JoinColumn``` 를 함께 사용한다면, unidirectional 관계를 갖는다. 예시는 아래와 같다.

![img](https://i.stack.imgur.com/ljaHg.png)

이 경우는 ```Post``` 엔티티에서만 ``@OneToMany`` 를 정의하면 된다.

``` java
@OneToMany(cascade = CascadeType.ALL, orphanRemoval = true)
@JoinColumn(name = "post_id")
private List<PostComment> comments = new ArrayList<>();
```

### Bidirectional one-to-many association

```@OneToMany``` 와 ```mappedBy``` 를 함께 쓴다면, bidirectional association 관계를 갖는다. 이 경우 ```PostComment``` 또한 ```Post``` 를 참조할수 있게 된다.

![img](https://i.stack.imgur.com/i5YWM.png) 

```PostComment``` 에서는, 다음과 같이 정의한다.

``` java
@ManyToOne(fetch = FetchType.LAZY)
private Post post;
```

```Post``` 에서는 다음과 같이 정의한다.

``` java
@OneToMany(
    mappedBy = "post",
    cascade = CascadeType.ALL,
    orphanRemoval = true
)
private List<PostComment> comments = new ArrayList<>();
```

```@OneToMany``` 측에서  ```mappedBy``` 를 선언해둠으로써, Hibernate는 bidirectional 관계가 ```ManyToOne``` 측에서 통제됨을 알게된다. 즉,  ```ManyToOne``` 측에서 테이블 관계의 기반인 Foreign Key column 값을 관리한다.

### 필요한 Utility method

bidirectional 관계에서는, 두가지 Utility 함수가 필요하다.

``` java
public void addComment(PostComment comment) {
    comments.add(comment);
    comment.setPost(this);
}

public void removeComment(PostComment comment) {
    comments.remove(comment);
    comment.setPost(null);
}
```

위 두 함수는 bidirectional 관계의 양쪽이 동기화되도록 보장한다. 양측을 모두 sync하지 않으면, hibernate는 association state 변화가 database에 전파되는것을 보장하지 않는다.

여기서 ```comment.setPost(this)``` 와 ```comments.remove(comment)``` 는 db에 직접적인 영향을 주지는 않는다. 하지만 ORM을 사용하는것이기 때문에 위와 같이 작성하는것이 관례이다. 

> 여기서 반드시 관계를 소유하고있는 객체에 변화를 가할때, db에 반영된다는 사실을 기억하자.

### 둘 중 어느것을 사용할 것인가?

Unidirectional ```@OneToMany``` 는 잘 성능이 좋지 못하므로, 피하는것이 좋다. bidirectional ```@OneToMany``` 를 사용하는것이 더 효율적이다.

## 출처
![https://stackoverflow.com/questions/11938253/jpa-joincolumn-vs-mappedby](https://stackoverflow.com/questions/11938253/jpa-joincolumn-vs-mappedby)