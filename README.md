# 점심-뭐-먹지

## 소개

오늘 점심 뭐먹지<br>
오늘의 점심을 추천해주는 서비스입니다.<br>
메뉴는 제작자가 근무하는 회사 주변의 음식점으로 한정되어 있습니다.<br>
Python3, macOS Sierra에서 정상적으로 실행되며, 다른 환경에서는 정상적인 실행을 보장할 수 없습니다.

## 실행 방법

```shell
$ python3 chooser.py
0: Stay Inside
1: Go Outside
2: No Matter
Give me a number: _
```

안에서 먹을지, 바깥에서 먹을지, 아니면 상관이 없는지, 각각의 옵션에 대응되는 숫자를 입력하시면 됩니다.<br>
argument를 실행 시 넘겨주는 것으로 보다 빠른 결과를 얻어낼 수 있습니다.<br>
(예시)

```shell
$ python3 chooser.py 2
생굴사랑(굴+순대국+추어탕)
```

## 잔디(업무용 메신저) 봇

`jandi-bot.py`와 `wolgeup.py`는 잔디 메신저를 사용할 때 활용할 수 있는 봇 서비스입니다.<br>
`jandi-bot.py`는 오늘의 추천 메뉴를, `wolgeup.py`는 급여일까지 얼마나 남았는지를 메시지로 알려줍니다.<br>
`jandiurl.py`를 같은 폴더 안에 생성해 주시고, `url='{your custom url}'`을 안에 입력해 주세요.<br>
URL은 잔디의 웹훅 서비스를 이용했을 때 얻을 수 있습니다.<br>
crontab을 이용하여 스케쥴링을 하시면 매일 필요한 시간에 스크립트를 실행시킬 수 있습니다.

## License

MIT License
