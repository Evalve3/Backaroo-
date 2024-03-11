from abc import ABC, abstractmethod

from src.dto.user.user import User


class IUserPresenter(ABC):

    @abstractmethod
    def get_user_presentation(self, user: User):
        pass
