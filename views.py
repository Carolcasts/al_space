from django.shortcuts import render

def index(request):
    return render(request, 'galeria_app/index.html')

def imagem(request):
    return render(request, 'galeria_app/imagem.html')