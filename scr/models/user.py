from tortoise import fields
from tortoise.models import Model


class User(Model):
    user_name = fields.CharField(
        max_length=20, unique=True, description="用户名称", index=True
    )
    user_password = fields.CharField(max_length=128, null=True, description="密码")

    user_role_id = fields.ManyToManyField("models.Role", related_name="user_name")
    ck_data = fields.TextField(max_length=10000, null=False, description="用户ck")
    user_phone = fields.CharField(max_length=500, null=False, description="用户手机号", index=True)
    create_time = fields.DatetimeField(null=False, description="创建时间")
    update_time = fields.DatetimeField(null=True, description="修改时间")

    class Meta:
        table = "user"
