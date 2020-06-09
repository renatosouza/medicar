from django.shortcuts import render
from rest_framework.response import Response
from drf_rw_serializers import generics
from .models import Especialidade
from .serializers import EspecialidadeListSerializer


class EspecialidadeList(generics.ListAPIView):
    read_serializer_class = EspecialidadeListSerializer
    
    def get_queryset(self):
        queryset = Especialidade.objects.all()
        search = self.request.query_params.get('search', None)
        if search:
            queryset = queryset.filter(nome__contains=search)
        return queryset