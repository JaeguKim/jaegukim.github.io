---
layout: post
title: "iTerm2 setting"
date: 2020-11-23 21:51:00 +0900
categories: [Settings]
---

- mac terminal setting guide
    - [link](https://medium.com/@Clovis_app/configuration-of-a-beautiful-efficient-terminal-and-prompt-on-osx-in-7-minutes-827c29391961)
    - [최종 zshrc 파일](https://github.com/Clovis-team/clovis-open-code-extracts/blob/master/utils/clovis-zshrc)

## iTerm2에서 source ~/.bash_profile 자동으로 실행되게 하기
1. Settings 열기(Cmd + ',' 단축키로도 가능))
2. General Tab에 Command 속성에 Send text at start 부분에 source ~/.bash_profile 입력

## iterm2에서 스크롤 휠 세팅

[https://stackoverflow.com/questions/36594420/how-can-i-turn-off-scrolling-the-history-in-iterm2](https://stackoverflow.com/questions/36594420/how-can-i-turn-off-scrolling-the-history-in-iterm2)

## bash/zsh global variable setting

[https://apple.stackexchange.com/questions/356441/how-to-add-permanent-environment-variable-in-zsh/356455#356455](https://apple.stackexchange.com/questions/356441/how-to-add-permanent-environment-variable-in-zsh/356455#356455)

## 한글 자소 분리 현상 해결
- Preferences > Profiles > Text > Unicode > Unicode normalization form
    - Unicode normalization form의 값으로 NFC를 선택

## Shortcut
| 설명 | 커멘드 
| --- | ---
| iTerm2 horizonal split | ``` cmd + shift + d ```
| iTerm2 vertical split | ``` cmd + d ```
| iTerm vertial pane navigation | ```cmd + [ or ] ```
