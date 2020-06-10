from django.db.models import Q
from rest_framework import serializers
from datetime import datetime, date
from django.contrib.auth.models import User
from .models import Especialidade, Medico, Horario, Agenda


class EspecialidadeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Especialidade
        fields = '__all__'
        
        
class MedicoSerializer(serializers.ModelSerializer):
    especialidade = EspecialidadeSerializer()
    
    class Meta:
        model = Medico
        fields = ('id', 'crm', 'nome', 
                  'especialidade', 'telefone', 'email')
        

class HorarioListSerializer(serializers.ListSerializer):
    
    def to_representation(self, data):
        data = data.exclude(valido=False)
        return super(HorarioListSerializer, self).to_representation(data)


class HorarioSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Horario
        fields = ('horario',)
        list_serializer_class = HorarioListSerializer
        
    
    # Mostra apenas hora e minuto, sem segundos
    def to_representation(self, instance):
        return str(instance.horario)[:5]
        
        
class AgendaSerializer(serializers.ModelSerializer):
    medico = MedicoSerializer()
    horarios = HorarioSerializer(many=True)
    
    class Meta:
        model = Agenda
        fields = ('id', 'medico', 'data', 'horarios')
        
        
class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}
        
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user