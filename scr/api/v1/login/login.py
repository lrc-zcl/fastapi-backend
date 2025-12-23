from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from service.auth_service import AuthService
from core.dependencies import get_user_info
from utils.schemas import UserInfo, RefreshTokenRequest

router = APIRouter()
auth_service = AuthService()

@router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    """用户登录"""
    try:
        tokens = await auth_service.log_in(
            form_data.username,
            form_data.password
        )
        if not tokens:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="用户名或密码错误"
            )
        return tokens
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"登录失败: {str(e)}"
        )

@router.post("/refresh")
async def refresh_token(request: RefreshTokenRequest):
    """刷新 Access Token"""
    try:
        # 注意：方法名是 refresh_token，不是 refresh_access_token
        tokens = await auth_service.refresh_token(request.refresh_token)
        if not tokens:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="刷新 Token 无效"
            )
        return tokens
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"刷新失败: {str(e)}"
        )

@router.get("/me")
async def get_me(current_user: UserInfo = Depends(get_user_info)):
    """获取当前用户信息"""
    return current_user