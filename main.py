from fastapi import FastAPI
from routes.todo import router as todo_router
from routes.params import router as params_router
# FastAPI 앱 생성
app = FastAPI()  # ASGI APP

# 라우터 등록
app.include_router(todo_router)
app.include_router(params_router)

#  요청 처리를 위한 엔드 포인트
@app.get("/")  #  GET메서드로 / url을 호출할 수 있는 엔드포인트
def hello():
    return {"message": "Hello FastAPI"}  # JSON 형식으로 응답 반환


# 모든 엔드포인트는 Swagger UI에 등록
# 만약 Swagger UI에 표시하고 싶지 않을 때
# include_in_schema 옵션을 False로 지정
@app.get("/hidden-endpoint", include_in_schema=False)
def hidden_endpoint():
    return {"message": "이 엔드포인트는 Swagger UI에 표시되지 않습니다"}
# 최상위 모듈로 실행될 때 uvicorn 서버를 실행시키고자 할 때


if __name__ == "__main__":
    import uvicorn
    # uvicorn을 모듈 경로로 실행
    uvicorn.run("main:app", host="127.0.0.1",
                port=8000, reload=True)