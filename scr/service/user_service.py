from typing import Union
from core.user import user_repository
from utils.response import SuccessResponse, FailedResponse
from utils.schemas import UserCreate, UserResponse, UserInfo


class UserService:
    def __init__(self):
        pass

    async def creat(self, user_data: UserCreate) -> Union[SuccessResponse, FailedResponse]:
        """创建用户"""
        try:
            obj = await user_repository.get_by_pnone(phone_number=user_data.user_phone)
            if obj:
                return FailedResponse(message="用户已存在")
            else:
                user_dict_data = user_data.model_dump(exclude={"user_role_id"})

                user_obj = await user_repository.create_user(user_dict_data)

                user_role_id = user_data.user_role_id

                await user_repository.update_roles(user_obj, user_role_id)
                
                # 将 User 对象转换为 UserResponse
                user_response = UserResponse(
                    id=user_obj.id,
                    user_name=user_obj.user_name,
                    user_phone=user_obj.user_phone,
                    ck_data=user_obj.ck_data,
                    create_time=user_obj.create_time,
                    update_time=user_obj.update_time
                )
                return SuccessResponse(data=user_response)
        except Exception as error:
            return FailedResponse(message=str(error))

    async def get_user_info(self, user_id: int) -> Union[SuccessResponse, FailedResponse]:
        """ 获取用户信息 """
        user_obj = await user_repository.get(user_id)
        if user_obj is None:
            return FailedResponse(message="用户不存在")
        else:
            await user_obj.fetch_related("user_role_id")
            roles = await user_obj.user_role_id.all()
            role_ids = [role.id for role in roles]

            user_info_data = UserInfo(
                user_name=user_obj.user_name,
                user_ck=user_obj.ck_data,
                user_role_id=role_ids
            )
            return SuccessResponse(data=user_info_data)

    def delete(self):
        pass

    def update_user_info(self):
        pass


user_service = UserService()
