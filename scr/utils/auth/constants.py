"""
JWT 认证相关常量配置
"""

# JWT 签名密钥
# ⚠️ 生产环境请修改此密钥，确保安全性
SECRET_KEY: str = "your-secret-key-change-in-production"

# JWT 签名算法
# HS256: 对称加密，使用同一个密钥签名和验证（适合单服务）
# RS256: 非对称加密，使用私钥签名，公钥验证（适合微服务）
ALGORITHM: str = "HS256"

# Token 过期时间
ACCESS_TOKEN_EXPIRE_MINUTES: int = 30  # Access Token 30分钟过期
REFRESH_TOKEN_EXPIRE_DAYS: int = 7     # Refresh Token 7天过期

# Token 类型常量
TOKEN_TYPE_ACCESS: str = "access"
TOKEN_TYPE_REFRESH: str = "refresh"

# OAuth2 配置
OAUTH2_TOKEN_URL: str = "/api/v1/auth/login"

