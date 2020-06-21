from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth.models import User
from django.urls import reverse


class MedicarAPITests(APITestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username='tester', 
                                             password='1234')
        self.client = APIClient()
        
        
    def test_get_token(self):
        url = reverse('api_token_auth')
        data = {'username': 'tester', 'password': '1234'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, 'token')
        
    def test_create_usuarios(self):
        url = reverse('register')
        data = {'username': 'tester2', 
                'email': 'tester2@test.com' , 
                'password': 'password'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)