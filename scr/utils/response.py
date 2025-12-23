from typing import Any, Generic, TypeVar, Optional, Union
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from tortoise import Model

ModelType = TypeVar("ModelType", bound=Model)
T = TypeVar("T")


class SuccessResponse(BaseModel, Generic[T]):
    code: int = 0
    message: str = "success"
    data: Optional[T] = None

    class Config:
        arbitrary_types_allowed = True


class FailedResponse(BaseModel, Generic[T]):
    code: int = -1
    message: str = "failed"
    data: Optional[T] = None

    class Config:
        arbitrary_types_allowed = True


class Success(JSONResponse, Generic[T]):
    def __init__(self, code: int = 0, msg: str = "success", data: T = None, **kwargs):
        content = {
            "code": code,
            "message": msg,
            "data": data
        }
        content.update(kwargs)
        super(Success, self).__init__(content=content, status_code=200)


class Failed(JSONResponse, Generic[T]):
    def __init__(self, code: int = -1, msg: str = "failed", data: T = None, **kwargs):
        content = {
            "code": code,
            "message": msg,
            "data": data
        }
        content.update(kwargs)
        super(Failed, self).__init__(content=content, status_code=200)
