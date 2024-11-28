from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from app.backend.db_depends2 import get_db

from typing import Annotated
#from app.models import Task
from app.models import*
from app.schemas2 import CreateTask, UpdateTask
#from app.schemas2 import *

from sqlalchemy import insert, select, update, delete
from slugify import slugify

router1 = APIRouter(prefix="/task", tags=["task"])

@router1.get("/")
async def all_tasks(db2: Annotated[Session, Depends(get_db)]):
    tasks = db2.scalars(select(Task)).all()
    return tasks

@router1.get("/task_id")
async def task_by_id(db2: Annotated[Session, Depends(get_db)],task_id: int):
    task = db2.scalar(select(Task).where(Task.id == task_id))
    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Task was not found'
        )
    return task



@router1.post("/create")
async def create_task(db2: Annotated[Session, Depends(get_db)], create_task: CreateTask, user_id: int):
    user = db2.scalar(select(User).where(User.id == user_id))
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='User was not found'
        )
    db2.execute(insert(Task).values(title=create_task.title,
                                    content=create_task.content,
                                    priority=create_task.priority,
                                    slug=slugify(create_task.title),
                                    user_id=user_id
                                    ))
    db2.commit()
    return {
        'status_code': status.HTTP_201_CREATED,
        'transaction': 'Successful'
    }



@router1.put("/update")
async def update_task(db2: Annotated[Session, Depends(get_db)], task_id: int, update_task: UpdateTask):
    task = db2.scalar(select(Task).where(Task.id == task_id))
    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Task was not found'
        )
    if update_task.title == "string":
        update_task.title = task.title
    if update_task.content == "string":
        update_task.content = task.content
    if update_task.priority == 0:
        update_task.priority = task.priority
    if update_task.user == 0:
        update_task.user = task.user_id

    db2.execute(update(Task).where(Task.id == task_id).values(title=update_task.title,
                                    content=update_task.content,
                                    priority=update_task.priority,
                                    slug=slugify(update_task.title),
                                    user_id=update_task.user
                                    ))
    db2.commit()
    return {
        'status_code': status.HTTP_201_CREATED,
        'transaction': 'Successful'
    }


@router1.delete("/delete")
async def delete_task(db2: Annotated[Session, Depends(get_db)], task_id: int):
    task = db2.scalar(select(Task).where(Task.id == task_id))
    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Task was not found'
        )
    db2.execute(delete(Task).where(Task.id == task_id))
    db2.commit()
    return {
        'status_code': status.HTTP_200_OK,
        'transaction': 'Category delete is successful'
    }

