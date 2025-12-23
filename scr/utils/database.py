"""
SQLite 数据库工具文件
用于初始化数据库连接和创建表结构
"""
import os
import sys
from tortoise import Tortoise
from pathlib import Path
from datetime import datetime

# 获取项目根目录和 scr 目录
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
SCR_DIR = os.path.dirname(os.path.dirname(__file__))  # scr 目录

# 将 scr 目录添加到 Python 路径，这样可以使用 models.user 这样的导入路径
if SCR_DIR not in sys.path:
    sys.path.insert(0, SCR_DIR)

DB_PATH = os.path.join(PROJECT_ROOT, "db.sqlite3")
DB_URL = f"sqlite://{DB_PATH}"

async def init_db():
    """
    初始化数据库连接并创建表结构
    """
    db_dir = os.path.dirname(DB_PATH)
    if db_dir and not os.path.exists(db_dir):
        os.makedirs(db_dir, exist_ok=True)
    
    await Tortoise.init(
        db_url=DB_URL,
        modules={
            'models': ['models.user', 'models.role']
        }
    )
    
    await Tortoise.generate_schemas()
    
    role = await init_default_roles()
    
    await init_default_user(role)
    
    print(f"数据库初始化成功！数据库文件位置: {DB_PATH}")

async def init_default_roles():
    """
    初始化默认角色数据
    如果 super_root 角色不存在，则创建它
    返回角色对象
    """
    from models.role import Role
    
    existing_role = await Role.filter(role_name="super_root").first()
    
    if not existing_role:
        role = await Role.create(
            role_name="super_root",
            role_description="超级管理员",
            is_super_root=True,
            create_time=datetime.now()
        )
        print("已创建默认角色: super_root (超级管理员)")
        return role
    else:
        print("默认角色 super_root 已存在，跳过创建")
        return existing_role

async def init_default_user(role):
    """
    初始化默认用户数据
    如果 admin 用户不存在，则创建它并关联 super_root 角色
    """
    from models.user import User
    
    existing_user = await User.filter(user_name="admin").first()
    if not existing_user:
        user = await User.create(
            user_name="admin",
            user_password="123456",
            ck_data="66668888",
            user_phone="13137741301",
            create_time=datetime.now()
        )

        await user.user_role_id.add(role)
        
        print("已创建默认用户: admin")
    else:
        print("默认用户 admin 已存在，跳过创建")

async def close_db():
    """
    关闭数据库连接
    """
    try:
        await Tortoise.close_connections()
        print("数据库连接已关闭")
    except Exception as e:
        # 忽略关闭时的取消错误（在 reload 模式下很常见）
        # 这些错误不影响应用功能，可以安全忽略
        pass


if __name__ == "__main__":
    import asyncio
    
    async def main():
        await init_db()
        await close_db()
    
    asyncio.run(main())

