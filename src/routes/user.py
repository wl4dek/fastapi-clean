from typing import List
from fastapi import APIRouter, Depends, Response, status
from dependency_injector.wiring import inject, Provide
from src.containers import Container
from src.services.user_service import UserService
from src.repositories.user_repository import NotFoundError
from src.schema.user import UserIn, UserOut

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.get('/status')
async def get_status():
    return {'status': 'OK'}


@router.get('', response_model=List[UserOut])
@inject
async def get_list(user_service: UserService = Depends(Provide[Container.user_service]),):
    return user_service.get_users()


@router.get('/{user_id}', response_model=UserOut)
@inject
async def get_by_id(user_id: int, user_service: UserService = Depends(Provide[Container.user_service]),):
    try:
        return user_service.get_user_by_id(user_id)
    except NotFoundError:
        return Response(status_code=status.HTTP_404_NOT_FOUND)


@router.post('', status_code=status.HTTP_201_CREATED, response_model=UserOut)
@inject
async def add(user_in: UserIn, user_service: UserService = Depends(Provide[Container.user_service])):
    return user_service.create_user(user_in)


@router.delete('/{user_id}', status_code=status.HTTP_204_NO_CONTENT)
@inject
async def remove(user_id: int, user_service: UserService = Depends(Provide[Container.user_service]),):
    try:
        user_service.delete_user_by_id(user_id)
    except NotFoundError:
        return Response(status_code=status.HTTP_404_NOT_FOUND)
    else:
        return Response(status_code=status.HTTP_204_NO_CONTENT)
