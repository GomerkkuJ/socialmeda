from sqlalchemy import Column, String, Integer, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from database import Base

#Таблица пользователей
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String)
    surname = Column(String)
    email = Column(String)
    phone_number = Column(String)
    city = Column(String)
    profile_photo = Column(String)
    password = Column(String)

    reg_date = Column(DateTime)
#Таблица публикаций
class UserPost(Base):
    __tablename__ = 'user_posts'
    id = Column(Integer, autoincrement=True, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    post_text = Column(String)

    publish_date = Column(DateTime)
    user_fk = relationship(User, lazy='subquery')

#Таблица фотографий
class PostPhoto(Base):
    __tablename__ = 'post_photos'
    id = Column(Integer, autoincrement=True, primary_key=True)
    post_id = Column(Integer, ForeignKey('user_posts.id'))
    post_photo = Column(String)

    post_fk = relationship(UserPost, lazy='subquery')

#Таблица комментарий
class Comment(Base):
    __tablename__ = 'post_comments'
    id = Column(Integer, autoincrement=True, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    post_id = Column(Integer, ForeignKey('user_posts.id'))
    comment_text = Column(String)

    user_fk = relationship(User, lazy='subquery')
    post_fk = relationship(UserPost, lazy='subquery')



