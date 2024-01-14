# TO-BE 레포로 공부하는 방법

> ✨이 저장소는 '코딩 테스트 합격자 되기(파이썬 편)' 을 연습 할 수 있는 저장소입니다. <br/>

<br/>
<br/>

<div align=center>
    <img src="asset/img/book.png" width="300px" height="auto" />
</div>

<br/>

## 😊 스터디 특징

> ✅ 해당 레포는 아무런 조건도 제약도 없는 자유로운 스터디 입니다. <br/>
> ✅ `PR` (Pull Request) 를 작성하면 자동으로 테스트가 동작합니다. <br/>
> ✅ 서로의 코드를 보면서 피드벡을 받으며 서로 으쌰으쌰 해봅시다. <br/>
> ✅ 로컬에서 디버깅 하면서 공부 할 수도 있습니다. <br/>

<br/>

## 🔥 저장소 유의사항

- 테스트에 사용하는 파이썬 버젼은 프로그래머스와 동일한 `python 3.8` 버젼입니다.
- 아래의 설명을 보면서 따라해 봅시다.
- 반드시 정해진 규칙에 따라서 `경로`, `파일 명` 및 `함수 명`을 작성해야 제대로 테스트가 동작합니다.
- 아이디는 깃허브 아이디를 의미합니다.

<br/>

## 서로서로 리뷰해 보자

- PR 을 생성하면 자동으로 스터디원중 한명이 리뷰어로 선택됩니다.
- 리뷰는 100% 자유입니다. 하면 좋고 아니여도 좋습니다.
- 다른 사람의 PR 을 보면서 공부하고 서로 소통해 보세요!

<br/>

## 알람 끄기

- 기본적으로 테스트 수행에 대한 알람이 이메일이 갑니다.
- 자주 알람이 오거나 필요없는 경우에는 해제 하시면 됩니다.
- 해당 저장소 화면 오른쪽 상단에 `Notifications` 을 `watch` 에서 `Ignore` 로 변경 해주세요.

<img src="asset/img/alarm.png" alt="Alt text" width="300px" height="auto" />

<br/>

## tests 폴더

- 기본이 되는 베이스를 완성해놨습니다.
- .gitignore 에 `tests` 폴더와 `.env` 파일이 추가해둔 상태입니다.
- 즉, 원하는 테스트 코드를 추가로 작성해보셔도 좋습니다.

<br/>

# ✨ 여기서 부터 해당 저장소를 사용하는 방법입니다.

## 0. 참여 방법

1. 책 저자님이 직접 운영하시는 소통 채널로 입장해주세요.
2. '통붕이' 또는 'tiaz0128' 또는 'TO-BE 스터디' 참여하고 싶다고 알려주세요.
3. 참여 의사가 있으신 분은 깃허브 아이디를 알려주세요.
4. 저장소 초대 메일이 가면 승인해주세요.

| 채널 | 링크 |
|----------|----------|
| 카카오톡 단톡방 | [링크](https://open.kakao.com/o/gX0WnTCf) |
| 디스코드 | [링크](https://discord.gg/3AfpGcTWr5) |

## 1. git clone

- 깃 clone 부터 시작하시면 됩니다!

```shell
git clone https://github.com/to-be-pass/to-be-pass-python-coding-test.git
```

<br/>

## 1. 챕터 깃 브랜치 생성

1. 해당 챕터 브랜치로 `checkout` 합니다.
2. 브랜치 명은 `아이디/ch_번호` 로 생성합니다.

```shell
git checkout ch_번호

git checkout -b 아이디/ch_번호
```

<br/>

## 2. solution 파일 생성 

1. `src/아이디/ch_번호` 폴더를 생성 합니다.
2. 챕터 5~9 는 반드시 앞에 0을 붙이고 폴더를 생성합니다. ex) ch_05, ch_06
3. 각 문제마다 정답 코드를 작성하는 파일을 생성합니다.
4. 파일 명은 `solution_문제번호.py` 로 작성합니다.

<br/>

## 3. solution 함수 작성

1. 함수 명은 `solution` 입니다.
2. 문제에서 주어지는 받아오는 매개변수를 적어줍니다.
3. 정답값을 리턴하는 함수를 작성합니다.

<br/>

## 4-1. 로컬에서 pytest 로 확인

1. `pytest`, `python-dotenv` 를 설치합니다.
2. 아래의 명령어로 `pytest` 를 실행합니다.
3. 실행 옵션은 자신의 아이디 와 해당주차 입니다.

```shell
pip install pytest python-dotenv

# 챕터 전체 문제 test 
pytest --id=아이디 -m ch_챕터번호

# 특정 문제만 test
pytest --id=아이디 -k 'test_문제번호'
```

<br/>

## 4-2. 로컬 디버깅 하기

- 로컬에서 자신이 작성 코드를 테스트 하고 싶은 경우 파일을 수정해야 합니다.
- `./tests/.env` 파일에 자신의 아이디값을 넣어줍니다.
- 다른 사람의 깃허브 아이디를 넣고 확인해 볼수 있습니다.
- 디버깅하면서 공부해보세요!

```text
USER_ID=아이디
```

<br/>

## 5. 브랜치 push

- 브랜치 명은 `아이디/ch_번호` 로 생성해서 `push` 합니다.

```shell
git push origin 아이디/ch_번호
```

<br/>

## 6. 또는 깃허브 PR(Pull Request) 생성해서 확인

<img src="asset/img/pr.png" alt="Alt text" width="550px" height="auto" />

- PR 을 생성 합니다.
- `ch_번호` 를 base 로 지정하고 `아이디/ch_번호` 를 compare 브랜치로 지정합니다.
- 깃허브에서 PR 작성하면 자동으로 테스트가 동작하고 정답을 확인합니다.

<br/>

<br/>

## 7-1. PR 테스트 실패 시

- PR 생성 후 `push` 할때마다 테스트가 동작합니다.
- PR 에서는 해당 챕터의 전체 문제를 테스트 합니다.
- 마지막까지 더 이상 문제를 풀지 못한 경우에는 강제로 `merge` 해줍니다.

<img src="asset/img/forced_merge.png" alt="Alt text" width="550px" height="auto" />

<br/>

## 7-1. PR 테스트 성공 시

- 테스트를 통과하면 `merge` 합니다.
- 시간이 있으면 다른 사람의 PR 을 보면서 공부하고 서로 소통해 보세요!

<br/>
