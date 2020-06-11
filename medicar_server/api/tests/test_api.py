from rest_framework.test import APITestCase, APIClient
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.contrib.auth.models import User
from django.urls import reverse
from api.models import Especialidade


class MedicarAPITests(APITestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username='tester', 
                                             password='1234')
        token = Token.objects.create(user=self.user)
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        self.especialidade1_data = {
            'nome': 'Pediatria'
        }
        self.especialidade2_data = {
            'nome': 'Ginecologia'
        }
        self.especialidade3_data = {
            'nome': 'Cardiologia'
        }
        self.especialidade4_data = {
            'nome': 'Clínico Geral'
        }
        Especialidade.objects.create(**self.especialidade1_data)
        Especialidade.objects.create(**self.especialidade2_data)
        Especialidade.objects.create(**self.especialidade3_data)
        Especialidade.objects.create(**self.especialidade4_data)
        
        
    def test_get_especialidades(self):
        url = reverse('especialidade_list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 4)
        
    def test_get_especialidades_filtradas(self):
        url = '/api/especialidades/?search=olo'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        
    