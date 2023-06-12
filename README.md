# `bewise.ai` первое тестовое задание

## Для начало работы необходимо

- Установить <a href="https://docs.docker.com/engine/install/" target="_blank">docker</a> (если не установлен)
- Установить <a href="https://docs.docker.com/compose/install/" target="_blank">docker-compose</a> (если не установлен)
- Запустить docker
- Убедиться, что 8000 и 5432 порты свободны
- Убедиться, что нет контейнеров с названиями app, db и alembic_migrations (Если у вас был установлен docker)

## Установка приложения

### 1. Клонируем репозиторий

    git clone https://github.com/rugnt/bewise.ai-problem-1.git

### 2. Переходим в директорию bewise.ai-problem-1

    cd bewise.ai-problem-1

### 3. Запускаем docker-compose

    sudo docker-compose up --build

### 4. Все готово. Открываем приложение <a href="http://localhost:8000/docs" target="_blank"> http://localhost:8000/docs </a>


## Пример работы


### После первого запуска делаем запрос к api. Но так как в бд нет данных, то api ничего не выводит
![1](https://github.com/rugnt/bewise.ai-problem-1/assets/93862774/d33461ab-cb95-4a11-a163-1ab0e4fa0c06)

### При повторном отправке запроса выводится последний сохранившейся вопрос

![2](https://github.com/rugnt/bewise.ai-problem-1/assets/93862774/22efaa43-a33f-4525-8f22-10e84adb8141)

## Обработка невозможного количества вопросов заданные в api
![3](https://github.com/rugnt/bewise.ai-problem-1/assets/93862774/18ef3209-7ea2-4eda-9beb-7ed9b469e38e)
![4](https://github.com/rugnt/bewise.ai-problem-1/assets/93862774/301dee14-bfba-4e89-8c66-68c5e9df6ffb)


## Делаем к api 10 запросов с количеством вопросов 100 (т.е в бд должно сохранится ещё 1000 вопросов)
![5](https://github.com/rugnt/bewise.ai-problem-1/assets/93862774/9012e6e7-b718-45d2-a5c5-2fff15890e8a)

## Смотрим сколько сохранилось записей в бд
![6](https://github.com/rugnt/bewise.ai-problem-1/assets/93862774/4003efb6-aa5e-4b94-91d3-8d118c2627e1)
