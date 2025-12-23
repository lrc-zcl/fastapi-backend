from typing import Union
from fastapi import APIRouter
from service.user_service import user_service
from utils.response import SuccessResponse, FailedResponse
from utils.schemas import UserCreate, UserResponse

api_router = APIRouter()


@api_router.get("/get_info", summary="获取用户信息", response_model=Union[SuccessResponse[UserResponse], FailedResponse])
async def get_user_info(user_id: int):
    user_obj = await user_service.get_user_info(user_id)
    return user_obj


@api_router.post("/create", summary="创建用户", response_model=Union[SuccessResponse[UserResponse], FailedResponse])
async def create_user(input_data: UserCreate):
    result = await user_service.creat(input_data)
    return result


    # @api_router.delete("/delete", summary="删除用户", response_model=Union[SuccessResponse, FailedResponse])
    # async def delete_user(user_id: int):
    #     try:
    #         await user_repository.delete(user_id)
    #         return Success()
    #     except Exception as error:
    #         return Failed(msg=str(error))
