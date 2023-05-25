import settings
import requests
import json

from requests.exceptions import RequestException

from typing import Any

from models.session import async_session
from models.database import Question

from fastapi import HTTPException

from sqlalchemy.engine.result import ChunkedIteratorResult
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy import func, select


def convert_questions_in_dict(questions: ChunkedIteratorResult) -> list[dict[str, Any]]:
    """Конвертирует список объектов Question в словарь"""
    result = []
    for question, in questions:
        result.append({
            'id': question.id,
            'question': question.question,
            'answer': question.answer,
        })
    return result


async def get_questions_for_api_and_save(question_num: int) -> list[dict[str, Any]]:
    """Основной функионал приложения"""
    if not 0 < question_num <= 100:
        raise HTTPException(status_code=422, detail='Введено недопустимое число вопросов')
    try:
        async with async_session() as session:
            # Записываем заранее возвращаемое значение
            questions_return = convert_questions_in_dict(
                await session.execute(
                    select(Question).order_by(Question.created_at.desc()).limit(settings.SIZE_OF_RETURNING_QUESTIONS)
                )
            )
            length = await session.scalar(select(func.count()).select_from(Question))
            required_size = min(length + question_num, settings.MAX_COUNT_QUESTIONS_IN_TABLE)

            # Записываем уникальные вопросы до тех пор, пока не будет добавлено length вопросов
            while length < required_size:
                question_num = required_size - length
                r = requests.get(f'https://jservice.io/api/random?count={question_num}')
                questions_from_api_service = json.loads(r.content)
                # Записываем все уникальные вопросы. Здесь используется list comprehension
                await session.execute(
                    insert(Question).values(
                        [
                            {
                                'id': question['id'],
                                'question': question['question'],
                                'answer': question['answer'],
                            }
                            for question in questions_from_api_service # list comprehension
                        ]
                    ).on_conflict_do_nothing(index_elements=['id'])
                )
                length = await session.scalar(select(func.count()).select_from(Question))
            return questions_return

    except RequestException as e:
        raise HTTPException(status_code=500, detail='Не удалось подключиться')
