from fastapi import Depends
from sqlalchemy.orm import Session

from src.db.session import get_db
from src.services.task import TaskService


def get_task_service(db: Session = Depends(get_db)) -> TaskService:
    return TaskService(db)
