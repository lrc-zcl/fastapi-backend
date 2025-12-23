from .base_crud import BaseCrud
from models.user import User
from models.role import Role
from typing import TypeVar, Optional, Type, Generic
from utils.schemas import UserResponse, RoleCreate
from datetime import datetime


class RoleRepository(BaseCrud):
    def __init__(self):
        super().__init__(model=Role)

    async def get_by_role_name(self, role_name: str) -> Role | None:
        return await self.model.filter(role_name=role_name).first()

    async def create_role(self, obj_in: RoleCreate) -> Role:
        obj = await self.create(obj_in)
        return obj

role_repository = RoleRepository()
