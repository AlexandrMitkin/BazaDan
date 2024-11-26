from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from app.backend.db_depends2 import get_db

from typing import Annotated
from app.models import User
from app.schemas2 import CreateUser, UpdateUser
#from app.models import *


from sqlalchemy import insert, select, update, delete
from slugify import slugify

router2 = APIRouter(prefix="/user", tags=["user"])

@router2.get("/")
async def all_users(db2: Annotated[Session, Depends(get_db)]):
    users = db2.scalars(select(User)).all()
    return users


@router2.get("/user_id")
async def user_by_id(db2: Annotated[Session, Depends(get_db)],user_id: int):
    try:
        user = db2.scalar(select(User).where(User.id == user_id))
    except:
        user = None
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='User was not found'
        )

    return user


@router2.post("/create")
async def create_user(db2: Annotated[Session, Depends(get_db)], create_user: CreateUser):
    db2.execute(insert(User).values(username="create_user.username"))

    # ,
    # firstname=create_user.firstname,
    # lastname=create_user.lastname,
    # age=create_user.age,
    # slug=slugify(create_user.username)
    db2.commit()
    return {
        'status_code': status.HTTP_201_CREATED,
        'transaction': 'Successful'
    }


@router2.put("/update")
async def update_user(db2: Annotated[Session, Depends(get_db)], user_id: int, update_user: CreateUser):
    user = db2.scalar(select(User).where(User.id == user_id))
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='User was not found'
        )
    db2.execute(update(User).where(User.id == user_id).values(
        username=update_user.username,
        firstname=update_user.firstname,
        lastname=update_user.lastname,
        slug=slugify(update_user.username),
        age=update_user.age))

    db2.commit()
    return {
        'status_code': status.HTTP_200_OK,
        'transaction': 'User update is successful!'
    }


@router2.delete("/delete")
async def delete_user(db2: Annotated[Session, Depends(get_db)], user_id: int):
    user = db2.scalar(select(User).where(User.id == user_id))
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='User was not found'
        )

    db2.delete(select(User).where(User.id == user_id))
    db2.commit()
    return {
        'status_code': status.HTTP_200_OK,
        'transaction': 'Category delete is successful'
    }