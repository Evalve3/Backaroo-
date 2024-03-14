from Application.views.user.schemas import ShowUserSchema
from src.dto.user.user import User
from src.abc.user.presenters.user_presenter import IUserPresenter


class UserPresenter(IUserPresenter):

    def get_user_presentation(self, user: User) -> ShowUserSchema:
        return ShowUserSchema(
            uid=user.uid,
            username=user.username,
            email=user.email,
            country=user.country.name if user.country else None,
            avatar_file_id=user.avatar_id,
            first_name=user.first_name,
            last_name=user.last_name,
            additional_info=user.additional_info,
            date_birth=user.date_birth
        )
