import pytest
import allure
import requests


@allure.feature('API Tests')
@allure.story('JSONPlaceholder')
class TestJSONPlaceholderAPI:

    BASE_URL = "https://jsonplaceholder.typicode.com"

    @allure.title("Get all posts")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.api
    def test_get_posts(self):
        with allure.step('Send GET request to /posts'):
            response = requests.get(f'{self.BASE_URL}/posts')

        with allure.step('Check status code == 200'):
            assert response.status_code == 200

        with allure.step('Check response contains list of posts'):
            json_data = response.json()
            assert isinstance(json_data, list)
            assert len(json_data) > 0

            allure.attach(str(json_data[:3]), 'First 3 posts', allure.attachment_type.JSON)

    @allure.title("Create new post")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.api
    def test_create_post(self):
        post_data = {
            "title": "foo",
            "body": "bar",
            "userId": 1
        }

        with allure.step(f'Send POST request to /posts with data: {post_data}'):
            response = requests.post(f'{self.BASE_URL}/posts', json=post_data)

        with allure.step('Check status code == 201'):
            assert response.status_code == 201

        with allure.step('Check response contains created data'):
            json_data = response.json()
            assert json_data['title'] == post_data['title']
            assert json_data['body'] == post_data['body']
            assert json_data['userId'] == post_data['userId']
            assert 'id' in json_data

            allure.attach(str(json_data), 'Created Post', allure.attachment_type.JSON)

    @allure.title("Update post")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.api
    def test_update_post(self):
        post_id = 1
        updated_data = {
            "id": 1,
            "title": "updated title",
            "body": "updated body",
            "userId": 1
        }

        with allure.step(f'Send PUT request to /posts/{post_id} with data: {updated_data}'):
            response = requests.put(f'{self.BASE_URL}/posts/{post_id}', json=updated_data)

        with allure.step('Check status code == 200'):
            assert response.status_code == 200

        with allure.step('Check data was updated'):
            json_data = response.json()
            assert json_data['title'] == updated_data['title']
            assert json_data['body'] == updated_data['body']

            allure.attach(str(json_data), 'Updated Post', allure.attachment_type.JSON)

    @allure.title("Delete post")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.api
    def test_delete_post(self):
        post_id = 1

        with allure.step(f'Send DELETE request to /posts/{post_id}'):
            response = requests.delete(f'{self.BASE_URL}/posts/{post_id}')

        with allure.step('Check status code == 200'):
            assert response.status_code == 200