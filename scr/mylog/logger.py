import os
import sys
from loguru import logger
from datetime import datetime


def setup_logger():
    """初始化全局日志配置"""

    log_dir = "../logs"
    os.makedirs(log_dir, exist_ok=True)
    current_time = datetime.now().strftime("%Y%m%d")

    logger.remove()

    logger.add(
        f"{log_dir}/{current_time}_log.log",
        rotation="10 MB",
        retention="100 days",
        encoding="utf-8",
        enqueue=True,
        format="{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {name}:{function}:{line} - {message}",
        backtrace=True,
        diagnose=True
    )
    logger.add(
        sys.stderr,
        colorize=True,
    )
    return logger


mylogger = setup_logger()

__all__ = ["mylogger"]