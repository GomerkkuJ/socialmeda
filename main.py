from fastapi import FastAPI
from starlette.staticfiles import StaticFiles

from photo.photo_api import photo_router
from comments.comment_api import comment_router
from post.user_post_api import posts_router
from user.user_api import user_router

#Для запуска дб
from database import Base, engine
Base.metadata.create_all(bind=engine)

app = FastAPI(docs_url='/')

# Регистрация компонентов
app.include_router(user_router)
app.include_router(posts_router)
app.include_router(photo_router)
app.include_router(comment_router)

# Добавление ссылки для открытия локальных файлов
app.mount(path='/media', app=StaticFiles(directory='media'))


@app.get('/hello')
async def hello():
    return {'message': 'Hello world'}