from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from app.backend.db_depends2 import get_db

from typing import Annotated
from app.models import Task
from app.schemas2 import CreateTask, UpdateTask

from sqlalchemy import insert, select, update, delete
from slugify import slugify

router1 = APIRouter(prefix="/task", tags=["task"])

@router1.get("/")
async def all_tasks():
    pass
# async def all_tasks(db2: Annotated[Session, Depends(get_db)]):
#     tasks = db2.scalars(select(Task)).all()
#     return tasks

@router1.get("/task_id")
async def task_by_id():
    pass
# async def task_by_id(db2: Annotated[Session, Depends(get_db)],task_id: int):
#     task = db2.scalar(select(Task).where(Task.id == task_id))
#     if task is None:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail='Task was not found'
#         )
#     return task


@router1.post("/create")
async def create_task(db2: Annotated[Session, Depends(get_db)]):
    pass


@router1.put("/update")
async def update_task(db2: Annotated[Session, Depends(get_db)]):
    pass


@router1.delete("/delete")
async def delete_task(db2: Annotated[Session, Depends(get_db)]):
    pass