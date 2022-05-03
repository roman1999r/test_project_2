import pytest
import requests
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from users.models import User
from users.serializers import UserDetailSerializer


@pytest.mark.asyncio
async def test_user_list():
    response = requests.get('http://127.0.0.1:8000/user-list')
    print(response.text)
    assert response.json() != []


@pytest.mark.asyncio
async def test_detail_user():
    response = requests.get('http://127.0.0.1:8000/user/1')
    print(response)
    assert response.status_code == status.HTTP_200_OK


class ListUserTest(APITestCase):
    def setUp(self):
        User.objects.create_user(username='roman', email='roman@roman.com', password='123')

    def test_user_list(self):
        response = self.client.get(reverse('users-list'))
        print(response.data, 'Response')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

class CreateUserTest(APITestCase):
    def setUp(self):
        self.data = {'username': 'mike', 'email': 'email@emal.com', 'password': '123'}

    def test_can_create_user(self):
        response = self.client.post(reverse('user-list'), self.data)
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ReadUserTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user('john', 'john@snow.com', '123')

    def test_can_read_user_detail(self):
        response = self.client.get(reverse('user-detail', args=[self.user.id]))
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data['id'], self.user.id)
        self.assertEqual(response.data['id'], self.user.id)


class UpdateUserTest(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser('john', 'john@snow.com', 'johnpassword')
        self.client.login(username='john', password='johnpassword')
        self.user = User.objects.create(username="rom", email="mail@mail.com", password="123")
        self.data = UserDetailSerializer(self.user).data
        print(self.data)
        self.data.update({'username': 'Changed'})

    def test_can_update_user(self):
        response = self.client.put(reverse('user-detail', args=[self.user.id]), self.data)
        print(response.data)

class DeleteUserTest(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser('john', 'john@snow.com', 'johnpassword')
        self.client.login(username='john', password='johnpassword')
        self.user = User.objects.create(username="mikey")

    def test_can_delete_user(self):
        response = self.client.delete(reverse('user-detail', args=[self.user.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        
