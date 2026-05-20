from sqlalchemy.orm import Mapped, mapped_column

from src.schemas.task import TaskSchema

from .base import Base


class TaskORM(Base):
    __tablename__ = "tasks"
    title: Mapped[str]
    completed: Mapped[bool] = mapped_column(default=False)

    def to_read_model(self) -> TaskSchema:
        return TaskSchema(id=self.id, title=self.title, completed=self.completed)
