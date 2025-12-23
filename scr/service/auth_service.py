from typing import Optional
from core.user import user_repository
from core.jwthandler import JwtHandler
from utils.schemas import UserInfo

class AuthService:

    async def log_in(self, user_name: str, user_passward: str) -> Optional[dict]:
        """用户登录"""

        try:
            # 先验证用户受否存在且密码正确
            user_obj = await user_repository.get_by_username(user_name)
            if not user_obj:
                raise Exception("当前用户不存在")
            else:
                passward = user_obj.user_password

                if passward != user_passward:
                    raise Exception("用户名密码不正确")
            input_data = {
                "user_id": user_obj.id,
                "user_name": user_name,
                "user_passward": user_passward,
                "user_role_id": user_obj.user_role_id
            }

            access_token = JwtHandler.create_access_token(input_data)
            refresh_token = JwtHandler.create_refresh_token(input_data)

            return {
                "access_token": access_token,
                "refresh_token": refresh_token,
                "token_type": "bearer"
            }
        except Exception as error:
            return None

    async def refresh_token(self, refresh_token: str) -> Optional[dict]:
        """ 刷新access token"""
        try:
            payload = JwtHandler.vertify_token(refresh_token)
            if not payload or payload.get("type") != "refresh":
                raise Exception("刷新token 无效")

            input_token_data = {
                "user_id": payload.get("id"),
                "user_name": payload.get("user_nameb"),
                "user_passward": payload.get("user_passward"),
                "user_role_id": payload.get("user_role_id")
            }

            new_access_token = JwtHandler.create_access_token(input_token_data)
            new_refresh_token = JwtHandler.create_refresh_token(input_token_data)
            return {
                "access_token": new_access_token,
                "refresh_token": new_refresh_token,
                "token_type": "bearer"
            }
        except Exception as error:
            return None

    async def get_user_from_token(self, token: str) -> UserInfo:
        """从 Token 中获取用户信息"""

        try:

            payload = JwtHandler.vertify_token(token)
            if not payload:
                raise Exception("Token 无效")
            user_name = payload.get("user_name")
            if not user_name:
                raise Exception("Token 中缺少用户信息")
            user_obj = await user_repository.get_by_username(user_name)
            if not user_obj:
                raise Exception("用户不存在")

            await user_obj.fetch_related("user_role_id")
            roles = await user_obj.user_role_id.all()
            role_ids = [role.id for role in roles]

            return UserInfo(
                user_name=user_obj.user_name,
                user_ck=user_obj.ck_data,
                user_role_id=role_ids
            )
        except Exception as error:
            raise Exception(f"获取用户信息失败: {str(error)}")
