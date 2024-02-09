from abc import ABCMeta
from abc import abstractmethod


class BaseAsyncUseCase(metaclass=ABCMeta):
    @abstractmethod
    async def execute(self, *args, **kwargs):
        pass
