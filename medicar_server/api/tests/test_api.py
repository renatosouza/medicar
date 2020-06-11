from rest_framework.test import APITestCase, APIClient
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.contrib.auth.models import User
from django.urls import reverse
from api.models import Especialidade, Medico, Agenda, Horario
from datetime import datetime, date, time, timedelta


class MedicarAPITests(APITestCase):
    
    def setUp(self):
        # Inicializa autenticacao
        self.user = User.objects.create_user(username='tester', 
                                             password='1234')
        token = Token.objects.create(user=self.user)
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        
        # Prepopula Especialidades
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
        
        # Prepopula Medicos
        medico1_data = {
            'nome': 'Drauzio Varella',
            'crm': 3711,
            'especialidade': especialidade1
        }
        medico2_data = {
            'nome': 'Gregory House',
            'crm': 2544,
            'especialidade': especialidade3
        }
        medico3_data = {
            'nome': 'Tony Tony Chopper',
            'crm': 3087,
            'especialidade': especialidade1
        }
        medico1 = Medico.objects.create(**medico1_data)
        medico2 = Medico.objects.create(**medico2_data)
        medico3 = Medico.objects.create(**medico3_data)
        
        # Prepopula Agendas
        ## Agenda valida
        agenda1_data = {
            'medico': medico3,
            'dia': (date.today()+timedelta(days=1)),
        }
        agenda1 = Agenda.objects.create(**agenda1_data)
        horario1_1_data = {
            'horario': '14:00',
            'agenda': agenda1
        }
        horario1_2_data = {
            'horario': '14:15',
            'agenda': agenda1
        }
        horario1_3_data = {
            'horario': '16:00',
            'agenda': agenda1
        }
        Horario.objects.create(**horario1_1_data)
        Horario.objects.create(**horario1_2_data)
        Horario.objects.create(**horario1_3_data)
        
        ## Agenda valida
        agenda2_data = {
            'medico': medico2,
            'dia': (date.today()+timedelta(days=1)),
        }
        agenda2 = Agenda.objects.create(**agenda2_data)
        horario2_1_data = {
            'horario': '09:00',
            'agenda': agenda2
        }
        horario2_2_data = {
            'horario': '09:30',
            'agenda': agenda2
        }
        horario2_3_data = {
            'horario': '14:00',
            'agenda': agenda2
        }
        Horario.objects.create(**horario2_1_data)
        Horario.objects.create(**horario2_2_data)
        Horario.objects.create(**horario2_3_data)
        
        ## Agenda invalida (data passada)
        agenda3_data = {
            'medico': medico1,
            'dia': (date.today() - timedelta(days=1))
        }
        agenda3 = Agenda.objects.create(**agenda3_data)
        horario3_1_data = {
            'horario': '10:00',
            'agenda': agenda3
        }
        Horario.objects.create(**horario3_1_data)
        
        ## Agenda invalida (sem horarios)
        agenda4_data = {
            'medico': medico1,
            'dia': (date.today()+timedelta(days=1)),
        }
        agenda4 = Agenda.objects.create(**agenda4_data)
        
        # Prepopula as consultas
        consulta1_data = {
            'agenda_id': 1,
            'horario': '14:00'
        }
        consulta2_data = {
            'agenda_id': 1,
            'horario': '16:00'
        }
        consulta3_data = {
            'agenda_id': 2,
            'horario': '09:30'
        }
        self.client.post('/consultas/', consulta1_data, format='json')
        self.client.post('/consultas/', consulta2_data, format='json')
        self.client.post('/consultas/', consulta3_data, format='json')
        
    
    # Testes no endpoint de Especialidades
    def test_get_especialidades(self):
        url = reverse('especialidade_list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 4)
        
    def test_get_especialidades_filtradas(self):
        url = '/especialidades/?search=olo'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
    
    
    # Testes no endpoint de Medicos    
    def test_get_medicos(self):
        url = reverse('medico_list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)
        
    def test_get_medicos_filtrados(self):
        url = '/medicos/?search=re&especialidade=1&especialidade=3'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        
        
    # Testes no endpoint de Agendas    
    def test_get_agendas(self):
        url = reverse('agenda_list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        
    def test_get_agendas_filtradas(self):
        data_inicio = date.today()
        data_fim = date.today() + timedelta(days=2)
        url = '/agendas/?medico=2&especialidade=3&data_inicio=%s&data_fim=%s' \
            % (data_inicio, data_fim)
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        
        
    # Testes no endpoint de Consultas
    def test_get_consultas(self):
        url = reverse('consulta_list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)
        
    def test_create_consulta(self):
        url = reverse('consulta_list')
        data = {
            'agenda_id': 2,
            'horario': '09:00',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
    def test_create_consulta_passado(self):
        url = reverse('consulta_list')
        data = {
            'agenda_id': 3,
            'horario': '10:00',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
    def test_create_consulta_existente(self):
        url = reverse('consulta_list')
        data = {
            'agenda_id': 1,
            'horario': '16:00',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
    def test_create_consulta_cliente_ocupado(self):
        url = reverse('consulta_list')
        data = {
            'agenda_id': 2,
            'horario': '14:00',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
    def test_delete_consulta(self):
        url = '/consultas/3/'
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        
    def test_delete_consulta_inexistente(self):
        url = '/consultas/10/'
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)