from datetime import datetime

from database import get_db
from database.models import User, UserAnswer, Rating


# Регистрация
def register_user_db(name: str, phone_number: str) -> int:
    # Сгенерировать подключение
    db = next(get_db())

    # Получить определенного пользователя
    exact_user = db.query(User).filter_by(phone_number=phone_number).first()

    # Если есть пользователь в базе
    if exact_user:
        return exact_user.id
    # Если нет пользователя в базе
    else:
        # Регистрируем
        new_user = User(name=name,
                        phone_number=phone_number,
                        reg_date=datetime.now())

        # Добавляем запись в базу
        db.add(new_user)
        # Сохраняем изменения
        db.commit()

        #Запись в таблицу рейтингов
        score_table = Rating(user_id=new_user.id)

        db.add(score_table)
        db.commit()

        return new_user.id

# Вывод результата
def get_user_score_db(user_id: int) -> int:
    db = next(get_db())

    checker = db.query(UserAnswer).filter_by(user_id=user_id, correctness=True).all()

    if checker:
        return len(checker)

    return 0

# Вывод лидеров
def show_leaders_db() -> list:
    db = next(get_db())
    rating = db.query(Rating).order_by(Rating.user_score.desc()).all()

    return rating[:5]


# Запись результатов пользователя
def add_user_answer_db(user_id, question_id, user_answer, correctness) -> bool:
    db = next(get_db())
    result = UserAnswer(user_id=user_id,
                        question_id=question_id,
                        user_answer=user_answer,
                        correctness=correctness,
                        answer_date=datetime.now())

    #Если ответил правильно на вопрос, то увеличить рейтинг
    exact_user_score = db.query(Rating).filter_by(user_id=user_id).first()
    if correctness:
        exact_user_score.user_score += 1

    else:
        exact_user_score.user_score -= 1


    db.add(result)
    db.commit()

    return True if correctness else False
