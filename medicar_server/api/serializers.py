from rest_framework import serializers
from .models import Especialidade


class EspecialidadeListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Especialidade
        fields = '__all__'