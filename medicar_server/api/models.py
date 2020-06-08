from django.db import models
from django.core.exceptions import ValidationError
from datetime import date


class Especialidade(models.Model):
    nome = models.CharField(max_length=40)

    class Meta:
        ordering = ['nome']

    def __str__(self):
        return self.nome


class Medico(models.Model):
    nome = models.CharField(max_length=40)
    crm = models.IntegerField()
    email = models.EmailField(blank=True)
    telefone = models.CharField(max_length=20, blank=True)
    especialidade = models.ForeignKey(Especialidade, 
                                      related_name='medicos', 
                                      on_delete=models.CASCADE)
    
    class Meta:
        ordering = ['nome']
    
    def __str__(self):
        return self.nome


class Agenda(models.Model):
    data = models.DateField()
    medico = models.ForeignKey(Medico, 
                               on_delete=models.CASCADE, 
                               unique_for_date='data')

    class Meta:
        ordering = ['data']

    def __str__(self):
        return '%s - %s' % (self.medico, self.data)

    def clean(self):
        if self.data < date.today() :
            raise ValidationError('Data passada!')
        


class Horario(models.Model):
    horario = models.TimeField()
    agenda = models.ForeignKey(Agenda, 
                               related_name='horarios', 
                               on_delete=models.CASCADE)
    
    class Meta:
        ordering = ['horario']


class Consulta(models.Model):
    data = models.DateField()
    horario = models.ForeignKey(Horario, on_delete=models.CASCADE)
    data_agendamento = models.DateTimeField(auto_now_add=True)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    cliente = models.ForeignKey('auth.User', 
                                related_name='consultas', 
                                on_delete=models.CASCADE)
    
    class Meta:
        ordering = ['data', 'horario']