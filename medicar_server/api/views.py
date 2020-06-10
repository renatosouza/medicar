from django.shortcuts import render
from django.db.models import Q, Count
from rest_framework import permissions
from drf_rw_serializers import generics
from datetime import datetime, date
from .models import Especialidade, Medico, Agenda, Horario
from .serializers import (
    EspecialidadeSerializer, MedicoSerializer, AgendaSerializer)


class EspecialidadeList(generics.ListAPIView):
    read_serializer_class = EspecialidadeSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        queryset = Especialidade.objects.all()
        search = self.request.query_params.get('search', None)
        if search:
            queryset = queryset.filter(nome__contains=search)
        return queryset
    
    
class MedicoList(generics.ListAPIView):
    read_serializer_class = MedicoSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        # Dados iniciais
        queryset = Medico.objects.all()
        
        # Filtra por parte do nome do medico
        search = self.request.query_params.get('search', None)
        if search:
            queryset = queryset.filter(nome__contains=search)
        
        # Filtra por especialidades
        especialidades = self.request.query_params.getlist('especialidade')
        especialidades = list(map(int, especialidades))
        if especialidades:
            or_condition = Q()
            for especialidade in especialidades:
                or_condition |= Q(especialidade=especialidade)
            queryset = queryset.filter(or_condition)
            
        return queryset
    

class AgendaList(generics.ListAPIView):
    read_serializer_class = AgendaSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        # Invalida os horarios de dias passados
        # e de hoje caso o horario ja tenha passado
        Horario.objects.filter(
            Q(agenda__data__lt=date.today()) 
            | (Q(agenda__data=date.today()) 
               & Q(horario__lt=datetime.now().time()))
            ).update(valido=False)
        # Invalida as agendas de datas passadas
        # ou aquelas sem horarios validos
        Agenda.objects.filter(
            Q(data__lt=date.today()) 
            | ~Q(horarios__valido=True)
            ).update(valida=False)
        
        # Dados iniciais
        queryset = Agenda.objects.filter(valida=True)
        
        # Filtra pelo id do medico
        medico = self.request.query_params.get('medico', None)        
        if medico:
            queryset = queryset.filter(medico=medico)
        
        # Filtra pelas especialidades dos medicos
        especialidades = self.request.query_params.getlist('especialidade')
        especialidades = list(map(int, especialidades))
        if especialidades:
            or_condition = Q()
            for especialidade in especialidades:
                or_condition |= Q(medico__especialidade=especialidade)
            queryset = queryset.filter(or_condition)
        
        # Filtra pelo intervalo de datas
        data_inicio = self.request.query_params.get('data_inicio', None)
        data_final= self.request.query_params.get('data_final', None)
        if data_inicio and data_final:
            
            queryset = queryset.filter(data__range=(data_inicio, data_final))
        
        return queryset