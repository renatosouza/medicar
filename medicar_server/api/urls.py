from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views


urlpatterns = [
    path('especialidades/', views.EspecialidadeList.as_view(), name='especialidade_list'),
    path('medicos/', views.MedicoList.as_view(), name='medico_list'),
    path('agendas/', views.AgendaList.as_view(), name='agenda_list'),
]

urlpatterns = format_suffix_patterns(urlpatterns)