from fastapi import APIRouter, Depends, HTTPException
from typing import List
from app.schemas.todo import TodoOut, TodoCreate, TodoUpdate
from app.dependencies.crud.todo import TodoCrud
from app.models.todo import Todo

router = APIRouter()


@router.post("/todos/", response_model=TodoOut)
def create_new_todo(todo: TodoCreate):
    crud = TodoCrud()
    return crud.create_todo(n_todo=todo)


@router.get("/todos", response_model=List[TodoOut])
def read_todos():
    crud = TodoCrud()
    return crud.get_todos()


@router.get('/{todo_id}', response_model=TodoOut)
def get_single_todo(todo_id: int):
    crud = TodoCrud()
    todo: Todo|None = crud.get_todo_by_id(todo_id=todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail='Todo not found.')
    return todo

@router.put('/{todo_id}/', response_model=TodoOut)
def update_todo(todo_id: int, u_dodo: TodoUpdate):
    crud = TodoCrud()
    todo: Todo|None = crud.update_todos(todo_id=todo_id, u_todo=u_dodo)
    if not todo:
        raise HTTPException(status_code=404, detail='Todo not found.')
    return todo

@router.delete('/{todo_id}/', response_model=TodoOut)
def delete_todo(todo_id: int):
    crud = TodoCrud()
    todo: Todo|None = crud.delete_todo(todo_id=todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail='Todo not found.')
    return todo
