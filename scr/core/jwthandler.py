import jwt
from typing import Optional
from datetime import datetime, timedelta
from copy import deepcopy
from utils.auth.constants import TOKEN_TYPE_ACCESS, ACCESS_TOKEN_EXPIRE_MINUTES, SECRET_KEY, ALGORITHM, \
    TOKEN_TYPE_REFRESH


class JwtHandler:
    """使用jwt生成token,刷新token,验证token(解析token)"""

    @staticmethod
    def create_access_token(inputda_data: dict, expire_time: Optional[timedelta] = None) -> str:
        """生成jwt token"""
        copy_data = deepcopy(inputda_data)
        duration_time = datetime.utcnow() + (expire_time or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
        init_time = datetime.utcnow()
        copy_data.update({
            "exp": duration_time,
            "iat": init_time,
            "type": TOKEN_TYPE_ACCESS
        })
        return jwt.encode(copy_data, SECRET_KEY, algorithm=[ALGORITHM])

    @staticmethod
    def create_refresh_token(inputda_data: dict, expire_time: Optional[timedelta] = None) -> str:
        """刷新 jwt token"""
        copy_data = deepcopy(inputda_data)
        duration_time = datetime.utcnow() + (expire_time or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES + 120))
        init_time = datetime.utcnow()
        copy_data.update({
            "exp": duration_time,
            "iat": init_time,
            "type": TOKEN_TYPE_REFRESH
        })
        return jwt.encode(copy_data, SECRET_KEY, algorithm=[ALGORITHM])

    @staticmethod
    def vertify_token(token: str) -> Optional[dict]:
        """验证解析token"""
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            return payload

        except:
            return None
