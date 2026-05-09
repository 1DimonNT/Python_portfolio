# tests/api/test_posts_api.py
import pytest
import allure
from api.client import APIClient
from api.posts_api import PostsAPI
from api.models import Post, CreatePostRequest, UpdatePostRequest
from config.settings import settings


@pytest.fixture(scope='module')
def api_client():
    return APIClient(settings.JSONPLACEHOLDER_URL)  # ← теперь берем из настроек


@pytest.fixture
def posts_api(api_client):
    return PostsAPI(api_client)


@allure.feature('API Tests')
@allure.story('JSONPlaceholder Posts')
class TestPostsAPI:

    @allure.title("Get all posts")
    @pytest.mark.api
    def test_get_all_posts(self, posts_api):
        posts = posts_api.get_all_posts()

        assert len(posts) > 0
        assert isinstance(posts[0], Post)
        assert posts[0].id == 1

    @allure.title("Get post by ID")
    @pytest.mark.api
    def test_get_post_by_id(self, posts_api):
        post = posts_api.get_post_by_id(1)

        assert post.id == 1
        assert post.userId == 1

    @allure.title("Create new post")
    @pytest.mark.api
    def test_create_post(self, posts_api):
        request = CreatePostRequest(
            title="foo",
            body="bar",
            userId=1
        )

        created_post = posts_api.create_post(request)

        assert created_post.title == "foo"
        assert created_post.body == "bar"
        assert created_post.userId == 1
        assert created_post.id is not None

    @allure.title("Update existing post")
    @pytest.mark.api
    def test_update_post(self, posts_api):
        request = UpdatePostRequest(
            id=1,
            title="updated title",
            body="updated body",
            userId=1
        )

        updated_post = posts_api.update_post(1, request)

        assert updated_post.title == "updated title"
        assert updated_post.body == "updated body"
        assert updated_post.id == 1

    @allure.title("Delete post")
    @pytest.mark.api
    def test_delete_post(self, posts_api):
        result = posts_api.delete_post(1)

        assert result is True

    @allure.title("Get posts by user ID")
    @pytest.mark.api
    def test_get_posts_by_user(self, posts_api):
        posts = posts_api.get_posts_by_user(1)
        assert len(posts) > 0
        for post in posts:
            assert post.userId == 1

    @allure.title("Check post exists")
    @pytest.mark.api
    def test_post_exists(self, posts_api):
        assert posts_api.post_exists(1) == True
        assert posts_api.post_exists(99999) == False