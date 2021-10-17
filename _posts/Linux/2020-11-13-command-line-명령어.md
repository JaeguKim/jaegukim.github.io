---
layout: post
title: "command-line 명령어"
date: 2020-11-13 13:29:00 +0900
categories: [Linux]
---

## ```~/``` 란 무엇인가?
```~/```란 /home/user_name을 의미한다.

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

## Bash commands

| 설명 | 커멘드 
| --- | ---
| 존재하지 않는 중간의 디렉토리를 자동으로 생성 | ``` mkdir -p [directory] ```
| 파일삭제 | ``` rm [file name] ```
| hidden file 리스팅 | ``` ls -a ```
| Bash history 검색 | ``` history ```
| Bash history 키워드로 검색 | ``` Ctrl + R ``` 후 검색, 다른 matcher 조회는 ```Ctrl +  R ```
| hidden file 리스팅 | ``` ls -a ```
| 현재 절대경로 표시 | ``` pwd ```
| ssh 접속후 disconnect | ``` exit ``` or ``` Ctrl - d ```
| 파일에 있는 내용 복사 | ``` cat original.txt ]] new.txt ```
| non-empty 디렉토리 삭제 | ``` rm -rf [folder name] ```
| process 죽이기 | ``` kill [pid] ```
| 디렉토리 내에 있는 모든 파일/디렉토리 복사 | ``` cp -r [source dir] ```
| 파일 이름 변경 | ``` mv old-name new-name ```
| 파일 옮기기 | ``` mv old-file new-file ```
| usermod [계정] -l [바꿀 계정] | 계정명을 바꿀 계정명 으로 변경합니다. (사용 비 권장)         |
| usermod -c [이름] [계정]    | 계정의 이름을 변경합니다.                                    |
| usermod -d ["경로"] [계정]    | 계정의 홈 디렉터리를 변경합니다.                             |
| usermod -s ["셸"] [계정]      | 계정의 로그인 기본 셸을 변경합니다.                          |
| usermod -e [날짜] [계정]      | 계정이 해당 날짜에 만료되도록 합니다.ex) usermod -e 2018-05-01 myuser |
| usermod -g [그룹] [계정]      | 사용자의 기본 소속 그룹을 변경합니다.                        |
| usermod -G [그룹] [계정]      | 계정의 소속 그룹을 변경합니다. 만약 여러 그룹을 지정할 때에는 ,(콤마) 로 구분하여 지정합니다. |
| usermod -a -G [그룹] [계정]   | 계정의 소속 그룹을 추가(add) 합니다.                         |
| list package installed | `apt list` [참고](https://www.cyberciti.biz/faq/apt-get-list-packages-are-installed-on-ubuntu-linux/)

## SED : Stream EDitor 

삽입,삭제,검색,replace(substitution) 가능

### 1. Replacing or substituting string

아래 커멘드는 "unix" 단어를 "linux"단어로 대체하는 커멘드이다.

``` sh
sed 's/unix/linux/' geekfile.txt
```

여기서 's'는 substitution 작업을 의미한다. 그리고 '/' 는 delimiter이다. 그리고 unix는 search pattern이고 linux는 replacement pattern이다. 기본적으로 패턴이 일치하는 첫번째 경우에 대해서만 작업이 수행되다.

#### 2. Replacing the nth occurrence of a pattern in a line

``` sh
sed 's/unix/linux/2' geekfile.txt
```

위는 두번째로 패턴이 일치하는 경우에 대해서 unix를 linux로 대체한다.

#### 3. Replacing all the occurrence of the pattern in line

패턴이 일치하는 모든 경우에 대해서, 작업을 수행하고 싶다면 다음과 같이 할수 있다.

``` sh
sed 's/unix/linux/g' geekfile.txt
```

#### 4. Replacing from nth occurrence to all occurrences in a line

다음은 3번째 부터 끝까지 일치하는 패턴에 대해서 작업을 수행하는 코드이다.

``` sh
sed 's/unix/linux/3g' geekfile.txt
```

#### [etc](https://www.geeksforgeeks.org/sed-command-in-linux-unix-with-examples/)

## Shell file 실행하기

``` sh
$ chmod +x script-name-here.sh
$ ./script-name-here
또는
$ sh script-name-here.sh
또는
$ bash script-name-here.sh
```