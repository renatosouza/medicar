from rest_framework import serializers
from .models import Especialidade, Medico


class EspecialidadeListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Especialidade
        fields = '__all__'
        
        
class MedicoListSerializer(serializers.ModelSerializer):
    especialidade = EspecialidadeListSerializer()
    
    class Meta:
        model = Medico
        fields = ('id', 'crm', 'nome', 'especialidade', 'telefone', 'email')