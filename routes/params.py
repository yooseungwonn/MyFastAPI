from fastapi import APIRouter, Query
# 기본적인 타입 힌트 이외의 복잡한 객체의 힌트는
# typing 모듈로부터 import 해야 한다
from typing import Optional, List
# Optional은 None을 허용하는 객체의 타입 힌트

router = APIRouter(tags=["/params"])

# 단일 쿼리 파라미터
# /items/?item_id=1
@router.get("/items/",
            description="단일 쿼리 파라미터")
async def read_items(item_id: int):
    return {"item_id": item_id}

# 여러 쿼리 파라미터를 받는 경우
# /users/?age=28&name=홍길동
# name은 필수로 전달 받지 않을 때


@router.get("/users/",
            description="여러 개의 쿼리 파라미터")
async def read_users(age: int,
                     name: Optional[str] = None):
    return {"name": name, "age": age}

# 쿼리 파라미터로 리스트를 받는 경우
# checkbox
# /items/multi/?item=아이템1&item=아이템2...


@router.get("/items/multi/",
            description="쿼리 파라미터로 리스트 받기")
async def read_items_multi(item: Optional[List[str]] = Query(None)):
    return {"items": item}


# 필수 쿼리 파라미터
# /search/?keyword=
# ... : Ellipse -> 필수 파라미터
@router.get("/search/")
async def search_item(keyword:str = Query(..., min_length=3)):
    return {"keyword": keyword}
