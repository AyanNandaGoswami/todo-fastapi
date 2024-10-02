from sqlalchemy.orm import Session
from typing import List, Optional
from app.schemas.todo import TodoCreate, TodoUpdate
from app.models.todo import Todo
from app.utils.crud import Crud


class TodoCrud(Crud):
    def create_todo(self, n_todo: TodoCreate) -> Todo:
        db_todo = Todo(name=n_todo.name, description=n_todo.description)
        self.db.add(db_todo)
        self.db.commit()
        self.db.refresh(db_todo)
        return db_todo

    def get_todos(self) -> List[Todo]:
        return self.db.query(Todo).all()

    def get_todo_by_id(self, todo_id: int) -> Optional[Todo]:
        return self.db.query(Todo).filter(Todo.id == todo_id).first()

    def update_todos(self, todo_id: int, u_todo: TodoUpdate) -> Todo:
        todo: Todo|None = self.get_todo_by_id(todo_id=todo_id)
        if todo:
            for key, value in u_todo.model_dump(exclude_unset=True).items():
                setattr(todo, key, value)
            self.db.commit()
            self.db.refresh(todo)
        return todo

    def delete_todo(self, todo_id: int) -> Optional[Todo]:
        todo: Todo | None = self.get_todo_by_id(todo_id=todo_id)
        if todo:
            self.db.delete(todo)
            self.db.commit()
        return todo
