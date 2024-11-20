from fastapi import APIRouter

router1 = APIRouter(prefix="/task", tags=["task"])

@router1.get("/")
async def all_tasks():
    pass

@router1.get("/task_id")
async def task_by_id():
    pass


@router1.post("/create")
async def create_task():
    pass


@router1.put("/update")
async def update_task():
    pass


@router1.delete("/delete")
async def delete_task():
    pass