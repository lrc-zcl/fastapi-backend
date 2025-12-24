from utils.schemas import UserInfo
from dependencies import get_user_info
from service.permission import permission_service
from fastapi import Depends, HTTPException, status


"""
使用方式和方法可以参考dependencies.py
"""

async def check_permission(user_info: UserInfo = Depends(get_user_info), current_url: str = None) -> UserInfo:
    """获取当前用户的信息"""
    has_permission = await permission_service.check_permission(user_info, current_url)

    if not has_permission:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="当前用户暂无使用该url的权限")

    return user_info
