from django.urls import path
from .views import home, tela

urlpatterns = [
    path('', home),
    path('tela/',tela)

]