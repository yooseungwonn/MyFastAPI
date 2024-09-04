from pydantic import BaseModel, Field
from typing import Optional

# Todo 아이템을 저장할 리스트
todos = []


# pydantic 스키마 생성
class Todo(BaseModel):
    id: Optional[int] = Field(None, json_schema_extra={
        "example": 1
    })
    title: str = Field(..., json_schema_extra={
        "example": "집에 가다가 마트에서 재료 사기"
    })
    done: bool = Field(False, json_schema_extra={
        "example": False
    })
    # 필드별로 example을 설정할 수도 있고,
    # 한번에 Config로 설정할 수도 있음
    model_config = {
        "json_schema_extra": {
            "example": {
                "id": 1,
                "title": "집에 가다가 마트에서 재료 사기",
                "done": False
            }
        }
    }