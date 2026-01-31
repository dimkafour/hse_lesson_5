from dataclasses import dataclass
from models.users import UserModel
from typing import Mapping
from typing import Sequence
from typing import Any
from repositories.users import UserRepository
from errors import UserNotFoundError


@dataclass(frozen=True)
class UserService:
    user_repo: UserRepository = UserRepository()

    async def register(self, values: Mapping[str, Any]) -> UserModel:
        return await self.user_repo.create(**values)


    async def login(self, login: str, password: str) -> UserModel:
        try:
            user = await self.user_repo.get_by_login_and_password(login, password)
            return user
        except UserNotFoundError:
            raise ValueError('Invalid login or password')
    

    async def get(self, user_id: int) -> UserModel:
        return await self.user_repo.get(user_id)


    async def delete(self, user_id: int) -> UserModel:
        return await self.user_repo.delete(user_id)


    async def deactivate(self, user_id: int) -> UserModel:
        return await self.user_repo.update(user_id, is_active=False)
    

    async def get_many(self) -> Sequence[UserModel]:
        return await self.user_repo.get_many()
