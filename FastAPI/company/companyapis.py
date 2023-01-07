from fastapi import APIRouter


router = APIRouter()

@router.get("/")
async def get_company_name():
    return {"company_name": "Exampe Company, LLC"}


@router.get("/employees")
async def num_of_employees():
    return 162