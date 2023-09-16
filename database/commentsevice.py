from datetime import datetime
from database import get_db
from database.models import Comment

# Опубликовать комментарий
def add_comment_db(post_id, text, user_id):
    db = next(get_db())
    new_comment = Comment(post_id=post_id,
                          comment_text=text,
                          user_id=user_id)
    db.add(new_comment)
    db.commit()
    return "Комментарий успено добавлен"

# Удалить комментарий
def delete_comment_db(comment_id):
    db = next(get_db())
    exact_post_comment = db.query(Comment).filter_by(id=comment_id).first()
    if exact_post_comment:
        db.delete(exact_post_comment)
        db.commit()
        return "Успешно удален"
    return False

# Изменить определенный комментарий
def change_comment_db(comment_id, new_comment):
    db = next(get_db())
    exact_post_comment = db.query(Comment).filter_by(id=comment_id).first()
    if exact_post_comment:
        exact_post_comment.comment_text = new_comment
        db.commit()
        return "Комментарий успешно изменен"
    return False


# получить все комменты определенного поста
def get_post_commencts(post_id):
    db = next(get_db())
    exact_post_comments = db.query(Comment).filter_by(post_id=post_id).all()
    return exact_post_comments