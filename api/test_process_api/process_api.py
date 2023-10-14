from fastapi import APIRouter

from database.testservice import add_question_db, get_20_questions_db
from database.userservice import add_user_answer_db

#Компонент
test_process_router = APIRouter(prefix='/test', tags=['Процесс прохождения теста'])

# Получить 20 вопросов
@test_process_router.get('/get-questions')
async def get_questions():
    result = get_20_questions_db()

    if result:
        return {'status': 1, 'questions': result}

    return {'status': 0, 'message': 'Вопросов пока нет в базе'}

# Проверка каждого ответа пользователя
@test_process_router.post('/check-answer')
async def check_answer(user_id: int, user_answer: int,
                       question_id: int, correctness: bool):
    result = add_user_answer_db(user_id, user_answer, question_id, correctness)

    return {'status': 1 if result else 0}


# Добавить вопрос
@test_process_router.post('/add-question')
async def add_question(q_text: str, answer: int,
                       v1: str, v2: str, v3:str = None, v4: str = None):
    result = add_question_db(q_text, answer, v1, v2, v3, v4)

    return {'status': 0, 'message': result}

