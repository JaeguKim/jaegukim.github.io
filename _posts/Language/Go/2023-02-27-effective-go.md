---
layout: post
title: "Effective Go"
date: 2023-02-27 11:37:00 +0900
categories: [Language,Go]
---

- Package name은 lower case, single-word names; there should be no need for underscores or mixedCaps
- Getters : Get을 prefix로 붙이지 않는다. Setter의 경우는 Set을 prefix로 붙일수 있다.
- Interface Names
  - one-method interface의 경우 `함수명 + er` 로 명명한다.
  - Read,Write,Close,Flush,String 등의 시그니쳐는 well-known type의 메소드와 동일한 의미를 지니고 있지 않다면 피한다.
- `rune` 이란 single Unicode code point에 대한 Go terminology이다.
- 여러번 defer를 호출할경우 LIFO order로 실행된다.
- new vs make
  - new는 포인터 타입을 반환하고 해당 타입의 field들은 zero로 초기화된다.
  - make는 slice,map,channel을 생성할때만 사용하고 필드들이 초기화된다.
- 2D array, slice 할당하는 2가지 방법
``` go
// Allocate the top-level slice.
picture := make([][]uint8, YSize) // One row per unit of y.
// Loop over the rows, allocating the slice for each row.
for i := range picture {
    picture[i] = make([]uint8, XSize)
}

// Allocate the top-level slice, the same as before.
picture := make([][]uint8, YSize) // One row per unit of y.
// Allocate one large slice to hold all the pixels.
pixels := make([]uint8, XSize*YSize) // Has type []uint8 even though picture is [][]uint8.
// Loop over the rows, slicing each row from the front of the remaining pixels slice.
for i := range picture {
    picture[i], pixels = pixels[:XSize], pixels[XSize:]
}
```
- Printing
  - `%v`(for "value") : the result is exactly what Print and Println would produce
  - `%+v` annotates the fields of the structure with their names
  - `%#v` prints the value in full Go syntax
- Initialization
  - Constants는 compiler에 의해 evaluatable할수 있어야 하며 `math.Sin`과 같이 런타임에 evaluatable한 함수를 사용해서 값을 할당할수는 없다.(constant expression 만 가능)
  - Variables는 general expression으로도 가능하다.
- Methods
  - Pointers vs Values
    - The rule about pointers vs. values for receivers is that value methods can be invoked on pointers and values, but pointer methods can only be invoked on pointers.
    - There is a handy exception, though. When the value is addressable, the language takes care of the common case of invoking a pointer method on a value by inserting the address the address operator automatically.
- Embedding
  - There's an important way in which embedding differs from subclassing. When we embed a type, the methods of that type become methods of the outer type, but when they are invoked the receiver of the method is the inner type, not the outer one.
  - Embedding types introuces the problem of name conflicts but the rules to resolve them are simple. First, a field or method X hides any other item X in a more deeply nested part of the type.
