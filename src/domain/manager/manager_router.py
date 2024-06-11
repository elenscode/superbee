from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status
from database import get_async_db
from domain.manager import manager_schema, manager_crud
from utils import mq

router = APIRouter(
    prefix="/api/manager",
)


@router.post(
    "/create",
    status_code=status.HTTP_201_CREATED,
    response_model=manager_schema.JobResponse,
)
async def job_create(
    object_create: manager_schema.JobCreate, db: Session = Depends(get_async_db)
):
    db_create = await manager_crud.create_answer(db, object_create)
    mq.send_to_rabbitmq(object_create.dict())
    return db_create
