"""
FastAPI 应用启动文件
"""
import os
import sys
from fastapi import FastAPI
from contextlib import asynccontextmanager

SCR_DIR = os.path.dirname(os.path.dirname(__file__))  
if SCR_DIR not in sys.path:
    sys.path.insert(0, SCR_DIR)

from utils.database import init_db, close_db
from api.v1.users.user_api import api_router as user_router
from api.v1.login.login import router as login_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    应用生命周期管理
    启动时初始化数据库，关闭时关闭数据库连接
    """
    await init_db() 
    yield
    try:
        await close_db()
    except Exception as e:
        pass

app = FastAPI(
    title="后端DEMO",
    description="后端项目",
    version="1.0.0",
    lifespan=lifespan
)

app.include_router(user_router, prefix="/api/v1/users", tags=["用户"])
app.include_router(login_router, prefix="/api/v1/auth", tags=["认证"])


@app.get("/")
async def root():
    """根路径"""
    return {"message": "FastAPI 服务运行中", "status": "ok"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "api.app:app",
        host="0.0.0.0",
        port=8866,
        reload=True,
        log_level="info"
    )

