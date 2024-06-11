from sqlalchemy import select
from sqlalchemy.orm import Session

from domain.manager.manager_schema import JobCreate
from models import Job
from typing import Optional


async def create_answer(db: Session, job_create: JobCreate) -> Optional[Job]:
    db_job = Job(
        subject=job_create.subject,
        content=job_create.content,
    )
    db.add(db_job)
    await db.commit()
    await db.refresh(db_job)
    return db_job
