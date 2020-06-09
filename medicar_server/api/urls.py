from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views


urlpatterns = [
    path('especialidades/', views.EspecialidadeList.as_view(), name='especialidade_list'),
]

urlpatterns = format_suffix_patterns(urlpatterns)