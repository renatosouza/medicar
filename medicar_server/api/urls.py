from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken.views import obtain_auth_token
from api import views


urlpatterns = [
    path('especialidades/', views.EspecialidadeList.as_view(), name='especialidade_list'),
    path('medicos/', views.MedicoList.as_view(), name='medico_list'),
    path('agendas/', views.AgendaList.as_view(), name='agenda_list'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('register/', views.UserCreate.as_view(), name='register'),
]

urlpatterns = format_suffix_patterns(urlpatterns)