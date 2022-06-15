from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('presupuesto', presupuesto, name='presupuesto'),
    path('contacto', contacto, name='contacto'),
]