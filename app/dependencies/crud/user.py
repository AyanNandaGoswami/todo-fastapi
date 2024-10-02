from typing import List

from app.schemas.user import CreateUser, UserOut
from app.models.user import User
from app.utils.crud import Crud


class UserCrud(Crud):

    def create_user(self, n_user: CreateUser) -> User:
        password = n_user.password
        # hash the password here
        db_user = User(first_name=n_user.first_name, last_name=n_user.last_name, email=n_user.email, is_active=True,
                       password=password)
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    def get_users(self) -> List[User]:
        return self.db.query(User).all()

