from django.contrib import admin
from .models import Especialidade, Medico, Agenda, Horario, Consulta


admin.site.register(Especialidade)
admin.site.register(Consulta)

@admin.register(Medico)
class MedicoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'crm', 'email', 'telefone', 'especialidade')


class HorarioInline(admin.TabularInline):
    model = Horario


@admin.register(Agenda)
class AgendaAdmin(admin.ModelAdmin):
    inlines = [HorarioInline]
    list_display = ('medico', 'dia')