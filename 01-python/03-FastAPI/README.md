# 가상환경 구축

## 왜 가상환경을 써야 할까?
web server를 구축할 때, Fast API 버전의 의존성 관리를 위해 가상환경에서 진행한다!

## venv
<b>V</b>irtual <b>ENV</b>ironment
가상환경을 만들어주는 파이썬의 모듈<br/>

프로젝트 루트 폴더에서 터미널 열고(vsc 내부 터미널 열 때 cmd + j) <br/>

* 가상환경 생성
``` bash
# mac
python -m venv .venv
```
``` bash
# window
virtualenv .venv
```

* 가상환경 활성화

``` bash
# mac
source .venv/bin/activate
```
``` bash
# window
## 파워쉘 실행 시 관리자 권한으로 실행
.venv/Scripts/activate
```

* 가상환경 종료
``` bash
deactivate
```
<br/>
<hr>
<br/>

# Fast API
* Starlette <br/>
비동기 방식을 가능하게 해주는 라이브러리

* Pydantic <br/>
데이터 타입을 지정하도록 하는 라이브러리

* Swagger <br/>

* Typer <br/>
CLI 개발 시 써보자

<br/>

<hr>

## 설치
``` bash
pip install fastapi
# mac
pip install 'uvicorn[standard]'
# window
# pip install uvicorn[standard]
```
``` bash
# 설치된 라이브러리 확인
pip list
```

## main.py
vsc에서는 루트 폴더를 기준으로 함. 만약 설치했는데도 모듈이 인식되지 않는다면, interpreter 선택하기 <br/>
cmd + shift + p -> python select interpreter 검색 -> .venv 선택 <br/>
그냥 맥북 자체 터미널 쓰는 중...🙃

* 실행
``` bash
python main.py
```
``` bash
uvicorn main:app --reload
```
<br/>
<hr>

# RESTful API

<b>C</b>reate POST <br>
<b>R</b>ead GET <br>
<b>U</b>pdate PUT <br>
<b>D</b>elete DELETE