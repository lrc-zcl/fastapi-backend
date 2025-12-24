from tortoise import fields
from tortoise.models import Model


class Role(Model):
    role_name = fields.CharField(
        max_length=20, unique=True, description="角色名称", index=True
    )
    role_description = fields.CharField(
        max_length=200, unique=True, description="角色描述", index=True
    )
    is_super_root = fields.BooleanField(default=False, description="是否为超级管理员")
    create_time = fields.DatetimeField(null=False, description="创建时间")
    allow_url_list = fields.JSONField(default=list, description="该角色允许访问的url地址")
    update_time = fields.DatetimeField(null=True, description="修改时间")

    class Meta:
        table = "role"

    def has_current_url_permission(self, current_url_path: str) -> bool:

        """检测该url是否在当前角色允许范围内"""
        if self.is_super_root:
            return True
        if not self.allow_url_list:
            return False
        if current_url_path in self.allow_url_list:
            return True

        for allowed_path in self.allow_url_list:
            if current_url_path.startswith(allowed_path):
                return True
        return False


