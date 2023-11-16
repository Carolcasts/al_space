from django.urls import path
from galeria_app.views import index, imagem

urlpatterns = [
    path('', index, name='index'),
    path('imagem/',imagem, name='imagem')
]