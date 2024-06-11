from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from domain.manager import manager_router

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    # allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(manager_router.router)
# app.include_router(answer_router.router)
# app.include_router(user_router.router)
# app.mount("/assets", StaticFiles(directory="frontend/dist/assets"))


@app.get("/")
def index():
    return {"message": "hello"}
