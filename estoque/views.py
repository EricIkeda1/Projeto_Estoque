from django.shortcuts import render, redirect
from .models import Produto
from django.db.models import Sum

def listar_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'listar_produtos.html', {'produtos': produtos})

def cadastrar_produto(request):
    if request.method == "POST":
        nome = request.POST.get('nome')
        quantidade = request.POST.get('quantidade')
        preco = request.POST.get('preco').replace('R$', '').replace(',', '.').strip()

        Produto.objects.create(
            nome=nome,
            quantidade=int(quantidade),
            preco=float(preco)
        )
        return redirect('listar_produtos')

    return render(request, 'cadastrar_produto.html')

def movimentacoes(request):
    return render(request, 'movimentacoes.html')

def relatorios(request):
    produtos = Produto.objects.all()

    total_itens = produtos.aggregate(Sum('quantidade'))['quantidade__sum'] or 0
    valor_total = sum(p.quantidade * p.preco for p in produtos)

    nomes = [p.nome for p in produtos]
    quantidades = [p.quantidade for p in produtos]

    context = {
        'produtos': produtos,
        'total_itens': total_itens,
        'valor_total': valor_total,
        'nomes': nomes,
        'quantidades': quantidades
    }
    return render(request, 'relatorios.html', context)

def listar_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'listar_produtos.html', {'produtos': produtos})

def relatorios(request):
    produtos = Produto.objects.all()

    total_itens = produtos.aggregate(Sum('quantidade'))['quantidade__sum'] or 0
    valor_total = sum(p.quantidade * p.preco for p in produtos)

    nomes = [p.nome for p in produtos]
    quantidades = [p.quantidade for p in produtos]

    context = {
        'produtos': produtos,
        'total_itens': total_itens,
        'valor_total': valor_total,
        'nomes': nomes,
        'quantidades': quantidades
    }
    return render(request, 'relatorios.html', context)