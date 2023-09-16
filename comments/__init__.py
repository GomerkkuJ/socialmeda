from pydantic import BaseModel


# Валидатор публикации коммента
class CommentModel(BaseModel):
    comment_text: str
    user_id: int
    post_id: int


# Валидатор на изменение коммента
class EditCommentModel(BaseModel):
    new_text: str
    comment_id: int