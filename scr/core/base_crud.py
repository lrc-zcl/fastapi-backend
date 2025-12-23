from tortoise import Model
from pydantic import BaseModel
from typing import TypeVar, Optional, Type, Generic

ModelType = TypeVar("ModelType", bound=Model)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class BaseCrud(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: Type[ModelType]):
        self.model = model

    async def create(self, input_dict: CreateSchemaType) -> Optional[ModelType]:
        """增加"""
        if not input_dict:
            return
        else:
            if isinstance(input_dict, dict):
                input_obj = input_dict
            else:
                input_obj = input_dict.model_dump()

        instance = self.model(**input_obj)
        await instance.save()
        return instance

    async def get(self, user_id: int) -> Optional[ModelType]:
        """根据id获取"""

        get_obj = await self.model.get(id=user_id)
        return get_obj if get_obj else None

    async def delete(self, user_id: int):
        """根据id删除"""
        try:
            pre_delete = await self.get(user_id)
            await pre_delete.delete()
        except Exception as error:
            raise error

    async def update(self, user_id: int, update_data: UpdateSchemaType) -> Optional[ModelType]:
        """根据id 进行更新"""
        pre_update = await self.get(user_id)
        if isinstance(update_data, dict):
            data = update_data
        else:
            data = update_data.model_dump()

        obj = await pre_update.update_from_dict(data)
        await obj.save()
        return obj
