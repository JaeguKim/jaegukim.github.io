---
layout: post
title: "command-line 명령어"
date: 2020-11-13 13:29:00 +0900
categories: [Linux]
---

## ```~/``` 란 무엇인가?
```~/```란 /home/user_name을 의미한다.

## iTerm2에서 source ~/.bash_profile 자동으로 실행되게 하기
1. Settings 열기(Cmd + ',' 단축키로도 가능))
2. General Tab에 Command 속성에 Send text at start 부분에 source ~/.bash_profile 입력

## export의 의미

### 예시 1

``` sh
export CONFLUENT_HOME="/Users/jaegu/confluent-6.0.0"
```

CONFLUENT_HOME 변수에 "/Users/jaegu/confluent-6.0.0" 값을 할당하고 그 값을 환경변수에 추가한다.

### 예시 2

``` sh
export PATH="/Users/jaegu/anaconda3/bin:$PATH"
```

$PATH - PATH 변수에 저장된 값
결과적으로 PATH는 다음과 같은 값을 갖게된다.

```
/Users/jaegu/anaconda3/bin:/Library/Frameworks/Python.framework/Versions/2.7/bin ...........
```
PATH 값앞에 ```/Users/jaegu/anaconda3/bin``` 값을 추가한것이다.

다음과 같은 방식도 가능하다.
``` sh
export PATH="$PATH:/Users/jaegu/anaconda3/bin"
```

이 경우는 기존의 PATH값뒤에 "Users/jaegu/anaconda3/bin" 을 추가하게 되므로 다음과 같은 값이 될것이다. 

```
/Library/Frameworks/Python.framework/Versions/2.7/bin ........... /Users/jaegu/anaconda3/bin:
```

## iterm2에서 스크롤 휠 세팅

[https://stackoverflow.com/questions/36594420/how-can-i-turn-off-scrolling-the-history-in-iterm2](https://stackoverflow.com/questions/36594420/how-can-i-turn-off-scrolling-the-history-in-iterm2)

## bash/zsh global variable setting

[https://apple.stackexchange.com/questions/356441/how-to-add-permanent-environment-variable-in-zsh/356455#356455](https://apple.stackexchange.com/questions/356441/how-to-add-permanent-environment-variable-in-zsh/356455#356455)

## Bash commands

| 설명 | 커멘드 
| --- | ---
| 파일삭제 | ``` rm [file name] ```
| hidden file 리스팅 | ``` ls -a ```
| Bash history 검색 | ``` history ```
| Bash history 키워드로 검색 | ``` Ctrl + R ``` 후 검색, 다른 matcher 조회는 ```Ctrl +  R ```
| hidden file 리스팅 | ``` ls -a ```
| iTerm2 horizonal split | ``` cmd + shift + d ```
| iTerm2 vertical split | ``` cmd + d ```
| 현재 절대경로 표시 | ``` pwd ```
| ssh 접속후 disconnect | ``` exit ``` or ``` Ctrl - d ```
| 파일에 있는 내용 복사 | ``` cat original.txt >> new.txt ```
| non-empty 디렉토리 삭제 | ``` rm -rf [folder name] ```
| process 죽이기 | ``` kill [pid] ```