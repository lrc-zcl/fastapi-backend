# 后端框架demo

一个基于 FastAPI 的用户和角色管理系统，使用 Tortoise ORM 和 SQLite 数据库。

## 功能特性

- ✅ 用户管理（创建、查询）
- ✅ 角色管理（多对多关系）
- ✅ 数据库自动初始化
- ✅ 默认超级管理员账户

## 技术栈

- **Web 框架**: FastAPI
- **ORM**: Tortoise ORM
- **数据库**: SQLite
- **Python 版本**: 3.8+

## 项目结构

```
fastApiProject/
├── scr/
│   ├── api/              # API 路由
│   │   ├── app.py        # FastAPI 应用入口
│   │   └── v1/
│   │       └── users/    # 用户相关 API
│   ├── core/             # 核心业务逻辑
│   │   ├── base_crud.py  # 基础 CRUD 操作
│   │   ├── user.py       # 用户仓储
│   │   └── role.py       # 角色仓储
│   ├── models/           # 数据模型
│   │   ├── user.py       # 用户模型
│   │   └── role.py       # 角色模型
│   ├── service/          # 业务服务层
│   │   └── user_service.py
│   └── utils/            # 工具类
│       ├── database.py   # 数据库配置
│       ├── schemas.py    # Pydantic 模型
│       └── response.py  # 响应格式
├── db.sqlite3            # SQLite 数据库文件
└── README.md
```

## 快速开始

### 1. 安装依赖

```bash
pip install -r requirment.txt -i https://pypi.doubanio.com/simple
```

### 2. 启动服务

```bash
cd scr
python api/app.py
```

### 3. 访问服务

- API 文档: http://localhost:8866/docs
- 根路径: http://localhost:8866/
