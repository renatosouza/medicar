from django.shortcuts import render
from django.db.models import Q
from rest_framework.response import Response
from drf_rw_serializers import generics
from .models import Especialidade, Medico
from .serializers import EspecialidadeListSerializer, MedicoListSerializer


class EspecialidadeList(generics.ListAPIView):
    read_serializer_class = EspecialidadeListSerializer
    
    def get_queryset(self):
        queryset = Especialidade.objects.all()
        search = self.request.query_params.get('search', None)
        if search:
            queryset = queryset.filter(nome__contains=search)
        return queryset
    
    
class MedicoList(generics.ListAPIView):
    read_serializer_class = MedicoListSerializer
    
    def get_queryset(self):
        queryset = Medico.objects.all()
        search = self.request.query_params.get('search', None)
        
        if search:
            queryset = queryset.filter(nome__contains=search)
        
        especialidades = self.request.query_params.getlist('especialidade')
        especialidades = list(map(int, especialidades))
        
        # Filtra pelos medicos que tem pelo menos uma das especialidades
        if especialidades:
            or_condition = Q()
            for especialidade in especialidades:
                or_condition |= Q(especialidade=especialidade)
            queryset = queryset.filter(or_condition)
            
        return queryset