import datetime
from typing import Union, Optional, Any
from pydantic import BaseModel, Field


class UserInfo(BaseModel):
    user_name: str = Field(description="用户名")
    user_ck: str = Field(description="用户ck")
    user_role_id: list[int] = Field(description="用户权限")


class UserCreate(BaseModel):
    user_name: str = Field(description="用户名")
    user_password: str = Field(description="用户密码")
    user_phone: str = Field(description="用户手机号")
    user_role_id: list[int] = Field(default_factory=list, description="用户角色id")
    ck_data: str = Field(description="用户ck")
    create_time: datetime.datetime = Field(default_factory=datetime.datetime.now, description="创建时间")
    update_time: Optional[datetime.datetime] = Field(default=None, description="更新时间")


class UserResponse(BaseModel):
    id: int = Field(description="用户ID")
    user_name: str = Field(description="用户名")
    user_phone: str = Field(description="用户手机号")
    ck_data: str = Field(description="用户ck")
    create_time: datetime.datetime = Field(description="创建时间")
    update_time: Optional[datetime.datetime] = Field(default=None, description="更新时间")


class RoleInfo(BaseModel):
    role_id: list[int] = Field(description="角色id")
    role_name: str = Field(description="角色名称")
    role_description: str = Field(description="角色描述")
    is_super_root: str = Field(description="是否为超级管理员")
    create_time: datetime.datetime = Field(description="创建时间")
    update_time: Optional[datetime.datetime] = Field(description="修改时间")


class RoleCreate(BaseModel):
    role_name: str = Field(description="角色名称")
    role_description: str = Field(description="角色描述")
    is_super_root: str = Field(description="是否为超级管理员")
    create_time: datetime.datetime = Field(description="创建时间")
    update_time: Optional[datetime.datetime] = Field(description="修改时间")


RoleResponse = Any


class RefreshTokenRequest(BaseModel):
    """刷新 Token 请求模型"""
    refresh_token: str = Field(description="刷新 Token")
