from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken.views import obtain_auth_token
from api import views


urlpatterns = [
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('register/', views.UserCreate.as_view(), name='register'),
    path('especialidades/', views.EspecialidadeList.as_view(), name='especialidade_list'),
    path('medicos/', views.MedicoList.as_view(), name='medico_list'),
    path('agendas/', views.AgendaList.as_view(), name='agenda_list'),
    path('consultas/', views.ConsultaList.as_view(), name='consulta_list'),
    path('consultas/<int:pk>/', views.ConsultaDetail.as_view(), name='consulta_detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)