---
layout: post
title: "Hackerrank - Java Regex 2 - Duplicate Words Solution 해설"
date: 2020-09-26 +0900
categories: [regex]
---
``` java
import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class JavaRegex2 {

    public static void main(String[] args) {

        String regex = "\\b([a-z]|[A-Z]+)(\\s+\\1\\b)+";
        Pattern p = Pattern.compile(regex, Pattern.CASE_INSENSITIVE);

        Scanner in = new Scanner(System.in);
        int numSentences = Integer.parseInt(in.nextLine());
        
        while (numSentences-- > 0) {
            String input = in.nextLine();
            
            Matcher m = p.matcher(input);
            
            // Check for subsequences of input that match the compiled pattern
            while (m.find()) {
                input = input.replaceAll(m.group(), m.group(1));
            }
            
            // Prints the modified sentence.
            System.out.println(input);
        }
        
        in.close();
    }
}
```

# Regex
- regular expression :  \b(\w+)(?:\W+\1\b)+
- \w : 한 글자 (word character): [a-zA-Z_0-9]
- \W : non-word charcter: [^\w]
- \b : word boundary
- \1 : 첫번째 괄호그룹과 매칭되는 부분(\w+)을 매칭한다
- \+ : 앞에나온 괄호그룹이 한번이상 나온것을 매칭한다
- \b 바운더리는 "Bob and Andy" ("and"가 두번 매칭되면 안됨) 와 같은 케이스를 없애기 위해서이다.

# Groups
``` java
input = inpuit.replaceAll(m.group(),m.group(1))
```
- 그룹전체를 첫번째 그룹으로 교체한다
- m.group : 전체 매칭
- m.group(i) : i번째 매칭, m.group(1)은 첫번째 매치이다.
- ?: -> (x)(?:y) 캡쳐하지 않는 그룹을 생성할 경우 ?:를 사용함, 결과값 배열에 캡쳐하지 않은 그룹은 들어가지 않음, 성능이 약간 빨라진다
