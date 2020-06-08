from django.contrib import admin
from .models import Especialidade, Medico, Agenda, Horario


admin.site.register(Especialidade)
admin.site.register(Medico)


class HorarioInline(admin.TabularInline):
    model = Horario


@admin.register(Agenda)
class AgendaAdmin(admin.ModelAdmin):
    inlines = [
        HorarioInline,
    ]