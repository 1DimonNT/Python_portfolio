# api/models.py
from dataclasses import dataclass
from typing import Optional


@dataclass
class Post:
    """Модель поста"""
    id: int
    title: str
    body: str
    userId: int

    def to_dict(self) -> dict:
        """Преобразовать в словарь"""
        return {
            'id': self.id,
            'title': self.title,
            'body': self.body,
            'userId': self.userId
        }

    @classmethod
    def from_dict(cls, data: dict) -> 'Post':
        """Создать из словаря"""
        return cls(
            id=data.get('id', 0),
            title=data.get('title', ''),
            body=data.get('body', ''),
            userId=data.get('userId', 0)
        )


@dataclass
class CreatePostRequest:
    """Модель запроса на создание поста"""
    title: str
    body: str
    userId: int

    def to_dict(self) -> dict:
        return {
            'title': self.title,
            'body': self.body,
            'userId': self.userId
        }


@dataclass
class UpdatePostRequest:
    """Модель запроса на обновление поста"""
    id: int
    title: str
    body: str
    userId: int

    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'title': self.title,
            'body': self.body,
            'userId': self.userId
        }
