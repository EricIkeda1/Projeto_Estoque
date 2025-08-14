from django.shortcuts import render

def listar_produtos(request):
    return render(request, 'listar_produtos.html')

def cadastrar_produto(request):
    return render(request, 'cadastrar_produto.html')

def movimentacoes(request):
    return render(request, 'movimentacoes.html')

def relatorios(request):
    return render(request, 'relatorios.html')
