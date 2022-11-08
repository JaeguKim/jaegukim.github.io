---
layout: post
title: "9 Password Storage Best Practices"
date: 2022-11-08 16:50:00 +0900
categories: [Security]
---

## 9 Password Storage Best Practices

1. Protect your databases and containers : DB나 컨테이너에 대한 접근을 보호

2. Hash all passwords : hash는 encryption key가 없으므로 원문으로 되돌릴수 없다.

3. Use a strong hash function

4. Salt your passwords : 원문 password에 랜덤스트링(salt)를 추가하여 해싱하라. 이때 원문 password와 salted password 간의 맵핑은 원격 저장소에 저장한다. 이 방법으 같은 패스워드라도 다르게 만들수 있다.

5. Pepper your password : 4번 방법과 유사하나 pepper string이 원격 저장소에 저장이 되지 않는다.

6. Update your work factors : 서버를 업그레이드하여 좀더 많은 암호화 작업을 할수 있도록 해라.

7. Dont't force users to reset passwords : 사용자에게 정기적으로 비밀번호를 변경하도록 하면, 사용자가 더 보안적으로 취약한 패스워드로 변경할 가능성을 높인다.

8. Check passwords for length, not complexity : password의 길이를 증가시키는것이 복잡도를 증가시키는것보다 더 안전성에 영향을 준다.

9. Check passwords against dictionaries and deny lists
