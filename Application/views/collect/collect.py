from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from Application.views.auth import get_current_user_from_token
from models.session import get_session
from src.dto.user.user import User

collect_router = APIRouter(prefix='/collect', tags=['collect'])


@collect_router.post('/')
async def create_collect(session: AsyncSession = Depends(get_session),
                         current_user: User = Depends(get_current_user_from_token)):
    pass
    # async with session.begin():
    #     # user_repo = UserRepoAlchemy(session=session)
    #     # presenter = UserPresenter()
    #     # create_user_case = CreateUserUC(user_repo=user_repo, user_presenter=presenter)
    #     # dto = CreateUserDTO(user=user_to_create)
    #     # res = await create_user_case.execute(dto=dto)
    #     #
    #     # if isinstance(res, ErrorResponse):  # очень важно проверять тип ответа внутри контекстного менеджера
    #     #     # чтобы транзакция откатилась если произошла ошибка
    #     #     raise HTTPException(
    #     #         status_code=res.code,
    #     #         detail=res.error
    #     #     )
    #
    # return res.data
