from fastapi import FastAPI, Body

from api.test_process_api.process_api import test_process_router
from api.user_api.api_user import user_router

#Создать бд
from database import Base, engine
Base.metadata.create_all(bind=engine)


# Обьект проекта
app = FastAPI(docs_url='/')

# Регистрация компонентов
app.include_router(user_router)
app.include_router(test_process_router)

@app.get('/hello')
async def hello():
    return {'message': 'Hello world'}

# Параметры для запросов
@app.get('/param-example')
async def param_example(user_id: int, user_answers: str):
    return {'message': f'У {user_id} 10 ответов {user_answers}'}

# Post
@app.post('/hello')
async def first_post(name: str, phone_number: int):
    return {name: phone_number}

# Body params
@app.put('/test-body')
async def test_body(header: str = Body(...),
                    main_text: str = Body(default='Пример текста')):
    return {'body_params': [header, main_text]}


# Запуск проекта на fastapi
# terminal: uvicorn main:app --reload
