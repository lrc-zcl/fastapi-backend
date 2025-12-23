from typing import Optional
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from service.auth_service import AuthService
from utils.schemas import UserInfo

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/api/v1/auth/login")  # 这个只是在API文档中使用,如果想对某个url添加身份登录认证,直接传递参数的时候加一个Depends即可

auth_service = AuthService()


async def get_user_info(token: str = Depends(oauth2_scheme)) -> UserInfo:
    """获取当前用户的信息"""
    try:
        user_info = await auth_service.get_user_from_token(token)
        return user_info
    except Exception as error:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=str(error)
        )
