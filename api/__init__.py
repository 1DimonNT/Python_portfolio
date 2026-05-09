# api/__init__.py
from api.client import APIClient
from api.posts_api import PostsAPI
from api.models import Post, CreatePostRequest, UpdatePostRequest

__all__ = [
    'APIClient',
    'PostsAPI',
    'Post',
    'CreatePostRequest',
    'UpdatePostRequest'
]