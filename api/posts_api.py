# api/posts_api.py
import allure
import time
from typing import List
from api.client import APIClient
from api.models import Post, CreatePostRequest, UpdatePostRequest


class PostsAPI:
    """API для работы с постами JSONPlaceholder"""

    def __init__(self, client: APIClient):
        self.client = client
        self.base_endpoint = "/posts"

    @allure.step("Get all posts")
    def get_all_posts(self) -> List[Post]:
        """Получить все посты"""
        response = self.client.get(self.base_endpoint)
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"

        posts_data = response.json()
        return [Post.from_dict(post) for post in posts_data]

    @allure.step("Get post by id: {post_id}")
    def get_post_by_id(self, post_id: int) -> Post:
        """Получить пост по ID"""
        response = self.client.get(f"{self.base_endpoint}/{post_id}")
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"

        return Post.from_dict(response.json())

    @allure.step("Create new post")
    def create_post(self, request: CreatePostRequest) -> Post:
        """Создать новый пост"""
        response = self.client.post(self.base_endpoint, data=request.to_dict())
        assert response.status_code == 201, f"Expected 201, got {response.status_code}"

        return Post.from_dict(response.json())

    @allure.step("Update post {post_id}")
    def update_post(self, post_id: int, request: UpdatePostRequest) -> Post:
        """Обновить пост"""
        response = self.client.put(f"{self.base_endpoint}/{post_id}", data=request.to_dict())
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"

        return Post.from_dict(response.json())

    @allure.step("Delete post {post_id}")
    def delete_post(self, post_id: int) -> bool:
        """Удалить пост"""
        response = self.client.delete(f"{self.base_endpoint}/{post_id}")
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"
        return True

    @allure.step("Get posts by user {user_id}")
    def get_posts_by_user(self, user_id: int) -> List[Post]:
        """Получить посты пользователя (с 1 ретраем при ошибках)"""
        for attempt in range(2):
            try:
                response = self.client.get(self.base_endpoint, params={'userId': user_id})
                assert response.status_code == 200, f"Expected 200, got {response.status_code}"
                posts_data = response.json()
                return [Post.from_dict(post) for post in posts_data]
            except Exception as e:
                if attempt == 0 and ('RemoteDisconnected' in str(e) or 'Connection' in str(e) or 'Timeout' in str(e)):
                    time.sleep(0.5)
                    continue
                raise
        return []

    @allure.step("Check post exists: {post_id}")
    def post_exists(self, post_id: int) -> bool:
        """Проверить, существует ли пост"""
        try:
            self.get_post_by_id(post_id)
            return True
        except AssertionError:
            return False