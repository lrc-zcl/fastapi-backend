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
    update_time = fields.DatetimeField(null=True, description="修改时间")
    class Meta:
        table = "role"
