from django.db import models


class Especialidade(models.Model):
    nome = models.CharField(max_length=40)


class Medico(models.Model):
    nome = models.CharField(max_length=40)
    crm = models.IntegerField()
    email = models.EmailField(blank=True)
    telefone = models.CharField(max_length=20, blank=True)
    especialidade = models.ForeignKey(Especialidade, 
                                      related_name='medicos', 
                                      on_delete=models.CASCADE)    


class Agenda(models.Model):
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    data = models.DateField()


class Horario(models.Model):
    horario = models.TimeField()
    agenda = models.ForeignKey(Agenda, 
                               related_name='horarios', 
                               on_delete=models.CASCADE)


class Consulta(models.Model):
    data = models.DateField()
    horario = models.ForeignKey(Horario, on_delete=models.CASCADE)
    data_agendamento = models.DateTimeField(auto_now_add=True)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    cliente = models.ForeignKey('auth.User', 
                                related_name='consultas', 
                                on_delete=models.CASCADE)