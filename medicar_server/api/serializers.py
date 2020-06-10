from django.db.models import Q
from rest_framework import serializers
from datetime import datetime, date
from django.contrib.auth.models import User
from .models import Especialidade, Medico, Horario, Agenda, Consulta


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
        fields = ('id', 'medico', 'dia', 'horarios')
        
        
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
    
    
class ConsultaCreateSerializer(serializers.Serializer):
    agenda_id = serializers.IntegerField()
    horario = serializers.TimeField()
    
    def validate(self, data):
        agenda = None
        horario = None
        try:
            agenda = Agenda.objects.get(id=data['agenda_id'], 
                                        valida=True)
            horario = Horario.objects.get(agenda=agenda.id, 
                                          horario=data['horario'], 
                                          valido=True)
        except Agenda.DoesNotExist:
            raise serializers.ValidationError('Data indisponível!')
        except Horario.DoesNotExist:
            raise serializers.ValidationError('Horario indisponível!')
        
        user = self.context['request'].user
        try:
            print(agenda.dia)
            consulta = Consulta.objects.get(dia=agenda.dia, 
                                            horario__horario=horario.horario, 
                                            cliente=user)
        except Consulta.DoesNotExist:
            return data
        
        raise serializers.ValidationError(
            'Cliente já tem consulta marcada nesse horário!')

    def create(self, validated_data):
        agenda = Agenda.objects.get(id=validated_data['agenda_id'])
        horario = Horario.objects.get(agenda=agenda.id,
                                      horario=validated_data['horario'])
        horario.valido = False
        horario.save()
        user = self.context['request'].user
        return Consulta.objects.create(dia=agenda.dia, 
                                       horario=horario, 
                                       medico=agenda.medico, 
                                       cliente=user)


class ConsultaSerializer(serializers.ModelSerializer):
    horario = HorarioSerializer()
    medico = MedicoSerializer()
    
    class Meta:
        model = Consulta
        fields = ('id', 'dia', 'horario', 'data_agendamento', 'medico',
                  'cliente')