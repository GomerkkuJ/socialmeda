from fastapi import APIRouter

from comments import CommentModel, EditCommentModel
from database.commentsevice import change_comment_db, add_comment_db, delete_comment_db, get_post_commencts

# Создать компонент
comment_router = APIRouter(prefix='/comment', tags=['Работа с комментариями'])


# запрос на публикацию комментария
@comment_router.post('/add_comment')
async def add_comment(data: CommentModel):
    result = add_comment_db(**data.model_dump())
    return {'status': 1, 'message': result}


# запрос на изменение комментария
@comment_router.put('/edit_comment')
async def edit_comment(data: EditCommentModel):
    result = change_comment_db(**data.model_dump())
    if result:
        return {'status': 1, 'message': result}
    return {'status': 0, 'message': 'Комментарий не найден'}


# запрос на удаление комментария
@comment_router.delete('/delete_comment')
async def delete_comment(comment_id: int):
    result = delete_comment_db(comment_id)
    if result:
        return {'status': 1, 'message': result}
    return {'status': 0, 'message': 'Сообщение удалено'}


# запрос на получение комментариев к определенной публикации
@comment_router.get('/get_comments')
async def get_comments(post_id: int):
    result = get_post_commencts(post_id)
    return {'status': 1, 'message': result}

