---
layout: post
title: "Passing Slice To Parameter"
date: 2022-07-27 13:43:00 +0900
categories: [Language,Go]
---

## Go lang parameter에 slice 전달하기

Go function에 전달된 파라미터들은 기본적으로 **value** 이다. slice를 주소로 넘기느냐 값으로 넘기느냐에 따라서 결과가 달라지는데 아래 예시를 보자.

``` go
func modifySlice(innerSlice []string) {
    fmt.Printf("%p %v   %p\n", &innerSlice, innerSlice, &innerSlice[0])
    innerSlice = append(innerSlice, "a")
    innerSlice[0] = "b"
    innerSlice[1] = "b"
    fmt.Printf("%p %v %p\n", &innerSlice, innerSlice, &innerSlice[0])
}

func main() {
    outerSlice := []string{"a", "a"}
    fmt.Printf("%p %v   %p\n", &outerSlice, outerSlice, &outerSlice[0])
    modifySlice(outerSlice)
    fmt.Printf("%p %v   %p\n", &outerSlice, outerSlice, &outerSlice[0])
}

// output
0xc00000c060 [a a]   0xc00000c080
0xc00000c0c0 [a a]   0xc00000c080
0xc00000c0c0 [b b a] 0xc000022080
0xc00000c060 [a a]   0xc00000c080
```

위 결과에서 보듯이 `innerSlice = append(innerSlice,"a")` 라인이 실행되어, slice의 길이가 변경이 되면 새로운 slice가 `innerSlice`에 할당되고 이후에 실행되는 라인은 새로 생성된 slice를 대상으로 수행된다. 즉 outerSlice와 innerSlice의 연결이 끊어지게 되는것이다.

이를 보완하기 위해서 아래와 같이 slice의 **pointer** 로 함수 파라미터에 전달할수 있다.

``` Go
func modifySlice(innerSlice *[]string) {
    *innerSlice = append(*innerSlice, "a")
    (*innerSlice)[0] = "b"
    (*innerSlice)[1] = "b"
    fmt.Println(*innerSlice)
}

func main() {
    outerSlice := []string{"a", "a"}
    modifySlice(&outerSlice)
    fmt.Print(outerSlice)
}

// output
[b b a]
[b b a]
```

### Summary

slice를 resize시키는 operation(eg. append)수행시에는 slice의 포인터를 함수에 전달하여 inner slice가 outer slice와 동일하게 할수 있다.
