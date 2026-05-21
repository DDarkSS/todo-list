from sqlalchemy.orm.session import Session

from src.repositories.task import TaskRepository
from src.schemas.task import TaskCreateSchema, TaskEditSchema, TaskSchema


class TaskNotFoundError(Exception):
    """Задача с указанным id не найдена."""


class TaskService:
    def __init__(self, db: Session) -> None:
        self.db = db
        self.task_repository = TaskRepository(db=db)

    def list_tasks(self) -> list[TaskSchema]:
        tasks = self.task_repository.get_all()
        return [TaskSchema.model_validate(task) for task in tasks]

    def create_task(self, new_task: TaskCreateSchema) -> TaskSchema:
        task = self.task_repository.create(title=new_task.title)
        self.db.commit()
        return TaskSchema.model_validate(task)

    def edit_task(self, id: str, payload: TaskEditSchema) -> TaskSchema:
        task_orm = self.task_repository.get_by_id(id)

        if task_orm is None:
            raise TaskNotFoundError(f"Task {id!r} not found")

        if payload.title:
            task_orm.title = payload.title

        if payload.completed is not None:
            task_orm.completed = payload.completed

        self.db.commit()

        return TaskSchema.model_validate(task_orm)

    def delete_task(self, id: str) -> None:
        task_orm = self.task_repository.get_by_id(id)

        if task_orm is not None:
            self.task_repository.delete(task_orm)
            self.db.commit()

        return None
