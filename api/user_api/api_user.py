from fastapi import APIRouter

from database.userservice import register_user_db, get_user_score_db, show_leaders_db


user_router = APIRouter(prefix='/user', tags=['Пользователи'])

# Регистрация пользователя
@user_router.post('/register')
async def register_user(name: str, phone_number: str):
    result = register_user_db(name, phone_number)

    return {'status': 1, 'user_id': result}


# Получить список лидеров
@user_router.get('/leaders')
async def get_5_leaders():
    result = show_leaders_db()

    return {'status': 1, 'leaders': result}


# Запись результата пользователя
@user_router.post('/done')
async def test_finished(user_id: int):
    result = get_user_score_db(user_id)

    if result:
        return {'status': 1, 'score': result}

    return {'status': 0, 'message': 'Пользователь не найден!'}

