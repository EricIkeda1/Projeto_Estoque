from django.shortcuts import render, redirect
from .models import Produto

def listar_produtos(request):
    return render(request, 'listar_produtos.html')

def cadastrar_produto(request):
    if request.method == "POST":
        nome = request.POST.get('nome')
        quantidade = request.POST.get('quantidade')
        preco = request.POST.get('preco').replace('R$', '').replace(',', '.').strip()

        Produto.objects.create(
            nome=nome,
            quantidade=quantidade,
            preco=preco
        )
        return redirect('listar_produtos')

    return render(request, 'cadastrar_produto.html')

def listar_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'listar_produtos.html', {'produtos': produtos})


def movimentacoes(request):
    return render(request, 'movimentacoes.html')

def relatorios(request):
    return render(request, 'relatorios.html')

from django.shortcuts import render, redirect
from .models import Produto


def listar_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'listar_produtos.html', {'produtos': produtos})
