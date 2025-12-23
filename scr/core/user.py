from datetime import datetime
from models.user import User
from .role import role_repository
from utils.schemas import UserCreate
from .base_crud import BaseCrud


class UserRepository(BaseCrud):
    def __init__(self):
        super().__init__(model=User)

    async def get_by_pnone(self, phone_number: str) -> User | None:
        return await self.model.filter(user_phone=phone_number).first()

    async def get_by_username(self, user_name: str) -> User | None:
        return await self.model.filter(user_name=user_name).first()

    async def create_user(self, obj_in: UserCreate) -> User:
        obj = await self.create(obj_in)
        return obj

    async def update_last_login(self, id: int) -> None:
        user = await self.model.get(id=id)
        user.update_time = datetime.now()
        await user.save()

    # async def authenticate(self, credentials: CredentialsSchema) -> Optional["User"]:
    #     user = await self.model.filter(username=credentials.username).first()
    #     if not user:
    #         raise HTTPException(status_code=400, detail="无效的用户名")
    #     verified = verify_password(credentials.password, user.password)
    #     if not verified:
    #         raise HTTPException(status_code=400, detail="密码错误!")
    #     if not user.is_active:
    #         raise HTTPException(status_code=400, detail="用户已被禁用")
    #     return user

    async def update_roles(self, user: User, role_ids: list[int]) -> None:
        try:
            await user.user_role_id.clear()
            for role_id in role_ids:
                role_obj = await role_repository.get(role_id)
                await user.user_role_id.add(role_obj)

        except Exception as error:
            raise error

    # async def reset_password(self, user_id: int) -> str:
    #     """重置用户密码，返回新密码"""
    #     user_obj = await self.get(id=user_id)
    #     if user_obj.is_superuser:
    #         raise HTTPException(status_code=403, detail="不允许重置超级管理员密码")
    #     # 生成安全的随机密码
    #     new_password = self._generate_secure_password()
    #     user_obj.password = get_password_hash(password=new_password)
    #     await user_obj.save()
    #     return new_password

    # def _generate_secure_password(self, length: int = 12) -> str:
    #     """生成安全的随机密码"""
    #     alphabet = string.ascii_letters + string.digits + "!@#$%^&*"
    #     password = "".join(secrets.choice(alphabet) for _ in range(length))
    #     return password


user_repository = UserRepository()
