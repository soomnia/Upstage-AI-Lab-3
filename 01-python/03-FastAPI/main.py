# 모듈이 인식이 안 되면
# cmd + shift + p -> python select interpreter -> .venv 선택
from fastapi import FastAPI, UploadFile, File

# app 객체 생성
app = FastAPI()

# router 연결
## books.py 에 생성한 router 사용
from books import router as books_router
app.include_router(books_router)

# 127.0.0.1:8000/
@app.get("/")
def index():
    return {"Hello":"World"}

from PIL import Image
from io import BytesIO
#predict.py에서 def predict() 호출
from predict import predict
@app.post("/predict/image")
# 유저가 파일을 업로드
## 파일이 클 경우, 파일이 다 읽히기 전에 진행되면 동기적으로 작동하는 파이썬에서 문제가 된다
## async로 파일이 다 읽힐 때까지 await
async def predict_image(file: UploadFile=File(...)):
    # IO형태로 파일을 주고 받음
    img = Image.open(BytesIO(await file.read()))
    result = predict(img)
    return result

# pip install python-multipart


# python main.py 로 실행했을 때 uvicorn 명령어로 실행시킨 것과 동일하게 하기 위함
if __name__ == "__main__":
    # ASGI 서버 실행 (비동기식)
    import uvicorn
    # main.py에서 app을 실행시켜줘
    uvicorn.run("main:app", reload=True)