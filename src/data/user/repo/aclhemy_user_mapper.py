from models.user.user_model import UserModel
from src.dto.user.user import User
from src.dto.category.category import Country


class UserMapper:

    @staticmethod
    def to_dto(user: UserModel) -> User:
        country = Country(**user.country.dict()) if user.country else None

        return User(
            username=user.username,
            first_name=user.first_name,
            last_name=user.last_name,
            date_birth=user.date_birth,
            email=user.email,
            avatar=user.avatar,
            profile_status=user.profile_status,
            additional_info=user.additional_info,
            sex=user.sex,
            adult_content=user.adult_content,
            registration_date=user.registration_date,
            country=country,
            is_active=user.is_active,
            uid=user.uid,
            hashed_password=user.hashed_password
        )

    @staticmethod
    def to_model(user: User) -> UserModel:
        country_uid = user.country.uid if user.country else None
        return UserModel(
            uid=user.uid,
            username=user.username,
            first_name=user.first_name,
            last_name=user.last_name,
            date_birth=user.date_birth,
            email=user.email,
            avatar=user.avatar,
            profile_status=user.profile_status,
            additional_info=user.additional_info,
            sex=user.sex,
            adult_content=user.adult_content,
            registration_date=user.registration_date,
            is_active=user.is_active,
            hashed_password=user.hashed_password,
            country_id=country_uid
        )
