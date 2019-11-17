from django.urls import path
from . import views

app_name = 'vacante'
urlpatterns = [
    path('validar/',views.ValidarView.as_view(),name = 'validar')
]