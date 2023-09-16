from fastapi import APIRouter
from user import RegisterUserModel, LoginUserModel, EditUserModel
from database.userservice import login_user_db, register_user_db, get_exact_users_db, get_all_users_db
# Создать компонент
user_router = APIRouter(prefix='/user', tags=['Управление пользователями'])


# запрос на вход в аккаунт
@user_router.post('/login')
async def login_user(data: LoginUserModel):
    result = login_user_db(**data.model_dump())
    return {'status': 1, 'message': result}


# запрос на регистрацию пользователя
@user_router.post('/register')
async def register_user(data: RegisterUserModel):
    result = register_user_db(**data.model_dump())
    if result:
        return {'status': 1, 'message': result}
    return {'status': 0, 'message': 'Пользователь с такой почтой есть в базе'}


# запрос на изменение информации пользователя
@user_router.put('/change_info')
async def change_info(data: EditUserModel):
    pass


# запрос на получение информации о пользователе
@user_router.get('/get_user')
async def get_user(user_id: int = 0):
    if user_id == 0:
        result = get_all_users_db()
        return {'status': 1, 'message': result}
    else:
        result = get_exact_users_db(user_id)
        return {'status': 1, 'message': result}