import models
from database import engine
from fastapi import FastAPI, Depends
from routers import auth, todos, users, address
from company import companyapis, dependencies

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(todos.router)
app.include_router(address.router)
app.include_router(users.router)
app.include_router(
    companyapis.router,
    prefix="/company_apis",
    tags=["company_apis"],
    dependencies=[Depends(dependencies.get_token_header)],
    responses={418: {"description": "Internal Use Only"}}
)
