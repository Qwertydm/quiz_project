from datetime import datetime

from database import get_db
from database.models import Question


# Функция добавления вопроса
def add_question_db(q_text, answer, v1, v2, v3, v4):
    db = next(get_db())

    new_question = Question(q_text=q_text, answer=answer, v1=v1, v2=v2,
                            v3=v3, v4=v4, reg_date=datetime.now())

    db.add(new_question)
    db.commit()

    return 'Вопрос был добавлен'

# Функция получения вопросов (20 шт.)
def get_20_questions_db():
    db = next(get_db())

    all_question = db.query(Question).all()

    return all_question[:20]

