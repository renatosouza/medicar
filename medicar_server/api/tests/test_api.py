from rest_framework.test import APITestCase, APIClient
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.contrib.auth.models import User
from django.urls import reverse
from api.models import Especialidade, Medico


class MedicarAPITests(APITestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username='tester', 
                                             password='1234')
        token = Token.objects.create(user=self.user)
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        especialidade1_data = {
            'nome': 'Pediatria'
        }
        especialidade2_data = {
            'nome': 'Ginecologia'
        }
        especialidade3_data = {
            'nome': 'Cardiologia'
        }
        especialidade4_data = {
            'nome': 'Clínico Geral'
        }
        especialidade1 = Especialidade.objects.create(
            **especialidade1_data)
        especialidade2 = Especialidade.objects.create(
            **especialidade2_data)
        especialidade3 = Especialidade.objects.create(
            **especialidade3_data)
        especialidade4 = Especialidade.objects.create(
            **especialidade4_data)
        
        self.medico1_data = {
            'nome': 'Drauzio Varella',
            'crm': 3711,
            'especialidade': especialidade1
        }
        self.medico2_data = {
            'nome': 'Gregory House',
            'crm': 2544,
            'especialidade': especialidade3
        }
        self.medico3_data = {
            'nome': 'Tony Tony Chopper',
            'crm': 3087,
            'especialidade': especialidade1
        }
        Medico.objects.create(**self.medico1_data)
        Medico.objects.create(**self.medico2_data)
        Medico.objects.create(**self.medico3_data)
        
        
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
        
    def test_get_medicos(self):
        url = reverse('medico_list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)
        
    def test_get_medicos_filtrados(self):
        url = '/api/medicos/?search=re&especialidade=1&especialidade=3'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)