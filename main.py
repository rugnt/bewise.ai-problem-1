import uvicorn
import settings

from fastapi import FastAPI
from services import get_questions_for_api_and_save
from typing import Any

app = FastAPI()


@app.get("/api/v1/questions")
async def save_and_return_last_questions(question_num: int) -> dict[str, list[dict[str, Any]]]:
    """Сохраняет в бд вопросы викторины по api
    https://jservice.io/api/random?count=1, и возвращает последние сохраненные"""
    questions = await get_questions_for_api_and_save(question_num)
    return {'questions': questions}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=settings.APP_PORT)
