from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def is_controle_estoque(user):
    return user.groups.filter(name='Controle de Estoque').exists()

@login_required
@user_passes_test(is_controle_estoque, login_url='/login/')
def listar_produtos(request):
    return render(request, 'listar_produtos.html')

@login_required
@user_passes_test(is_controle_estoque, login_url='/login/')
def cadastrar_produto(request):
    return render(request, 'cadastrar_produto.html')

@login_required
@user_passes_test(is_controle_estoque, login_url='/login/')
def movimentacoes(request):
    return render(request, 'movimentacoes.html')

@login_required
@user_passes_test(is_controle_estoque, login_url='/login/')
def relatorios(request):
    return render(request, 'relatorios.html')

@login_required
@user_passes_test(is_controle_estoque, login_url='/login/')
def painel_estoque(request):
    return render(request, 'painel_estoque.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('painel_estoque') 
        else:
            messages.error(request, 'Usuário ou senha inválidos.')
    return render(request, 'login.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')
