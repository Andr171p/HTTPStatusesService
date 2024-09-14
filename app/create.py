from fastapi import FastAPI

from app.api import router


app = FastAPI(
    title="User statuses API"
)

app.include_router(
    router=router,
    prefix="/api/statuses",
    tags=["statuses"]
)
