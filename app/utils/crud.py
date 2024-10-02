from app.dependencies.database import get_db


class Crud:

    def __init__(self) -> None:
        db_generator = get_db()
        db = next(db_generator)

        self.db = db

