from models.user import User
from core.role import role_repository


class PermissionService:

    async def check_permission(self, user: User, url_path: str) -> bool:

        """检查权限"""
        user_role_id = user.user_role_id
        if not user_role_id:
            return False

        for signal_role_id in user_role_id:
            signal_role_info = await role_repository.get(signal_role_id)
            if signal_role_info.has_current_url_permission(url_path):
                return True
        else:
            return False




permission_service = PermissionService()