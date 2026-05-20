from fastapi import APIRouter, Depends, status

from src.api.dependencies import get_task_service
from src.schemas.task import TaskCreateSchema, TaskEditSchema, TaskSchema
from src.services.task import TaskService

router = APIRouter(prefix="/tasks")


@router.get("", status_code=status.HTTP_200_OK)
def get_all_tasks(
    task_service: TaskService = Depends(get_task_service),
) -> list[TaskSchema]:
    return task_service.list_tasks()


@router.post("", status_code=status.HTTP_201_CREATED)
def add_task(
    payload: TaskCreateSchema, task_service: TaskService = Depends(get_task_service)
) -> TaskSchema:
    return task_service.create_task(payload)


@router.patch("/{id}", status_code=status.HTTP_200_OK)
def edit_task(
    id: str,
    payload: TaskEditSchema,
    task_service: TaskService = Depends(get_task_service),
) -> TaskSchema | None:
    return task_service.edit_task(id, payload)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(id: str, task_service: TaskService = Depends(get_task_service)) -> None:
    return task_service.delete_task(id)
