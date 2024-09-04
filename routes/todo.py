from fastapi import APIRouter
from fastapi import Path # Path Variable 객체
from fastapi import HTTPException
import schemas.todo as todo_schema
from schemas.todo import todos  #  할일 목록
from typing import List

# 라우터 생성
router = APIRouter(tags=['todos'])


# TODO 목록 불러오기
@router.get("/todos",
            response_model=List[todo_schema.Todo])
async def get_todos():
    return todos


# 새 TODO 생성
# 중복된 id가 없을 때 생성
# 중복된 id가 있을 때 생성하면 안되고 400 에러 발생
@router.post("/todos")
async def add_todo(todo: todo_schema.Todo):
    # 중복된 id가 있는지 확인
    for existing_todo in todos:
        if existing_todo.id == todo.id: # 이미 있다
            raise HTTPException(
                status_code=400,
                detail="해당 ID를 가진 Todo가 이미 있습니다."
            )
    # 중복되는 Todo가 없으므로 목록에 추가
    todos.append(todo) # 전달 받은 Todo를 목록에 추가
    return todo




# TODO 변경
@router.put("/todos/{todo_id}")
async def modify_todo(todo_id: int = Path(
    ...,  # 필수 필드
    title="Todo Id",
    description="수정할 Todo 아이템의 ID",
    ge=1,  # 1 이상
    le=100  # 100 이하
), updated_todo: todo_schema.Todo = None):
    # 목록에서 수정할 Todo Item을 찾기
    for existing_todo in todos:
        if existing_todo.id == todo_id: # 찾았음
            # 아이템 변경
            existing_todo.title = updated_todo.title
            existing_todo.done = updated_todo.done
            return existing_todo

    # 못 찾음 -> 404 오류 발생
    raise HTTPException(status_code=404,
                        detail="수정할 Todo Item을 찾지 못했습니다")



# TODO 삭제
# 목록에서 todo_id를 가진 Todo 항목이 있으면 삭제
#                            없으면 404 에러
@router.delete("/todos/{todo_id}")
async def delete_todo(todo_id:int=Path(
    ...,
    title="Todo Id",
    description="삭제할 Todo 아이템의 ID"
)):
    # 리스트에서 todo_id를 가진 항목을 찾기
    for index, todo in enumerate(todos):
        if todo.id == todo_id: # 삭제할 아이템 찾음
            # 리스트에서 항목 삭제
            deleted_todo = todos.pop(index)
            return { "todo_id": todo.id,
                     "deleted_todo": deleted_todo}

    # 삭제할 todo가 없을 때
    raise HTTPException(status_code=404,
                        detail="삭제할 Todo가 없습니다.")