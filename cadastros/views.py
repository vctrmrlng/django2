from django.shortcuts import render
from .models import Usuario, Produto

# render -> Renderização
# request -> Requisição -> GET -> buscar, POST -> Postar

# Create your views here.
def listar_usuarios(request):
    usuarios = Usuario.objects.all() #Acessa todos os usuários cadastrados do model Usuario
    return render(request, 'listar_usuarios.html', {'usuarios' : usuarios})

def listar_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'listar_produtos.html', {'produtos' : produtos})