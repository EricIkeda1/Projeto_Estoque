from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Sum
from .models import Produto, Movimentacao

def listar_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'listar_produtos.html', {'produtos': produtos})

def cadastrar_produto(request):
    if request.method == "POST":
        nome = request.POST.get('nome')
        quantidade = int(request.POST.get('quantidade'))
        preco = float(request.POST.get('preco').replace('R$', '').replace(',', '.').strip())

        produto = Produto.objects.create(
            nome=nome,
            quantidade=quantidade,
            preco=preco
        )

        Movimentacao.objects.create(
            produto=produto,
            tipo='entrada',
            quantidade=quantidade
        )

        return redirect('listar_produtos')

    return render(request, 'cadastrar_produto.html')

def movimentacoes(request):
    movimentacoes = Movimentacao.objects.select_related('produto').order_by('-data')
    return render(request, 'movimentacoes.html', {'movimentacoes': movimentacoes})

def dar_baixa_produto(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)

    if request.method == "POST":
        quantidade = int(request.POST.get('quantidade'))
        if 0 < quantidade <= produto.quantidade:
            produto.quantidade -= quantidade
            produto.save()

            Movimentacao.objects.create(
                produto=produto,
                tipo='saida',
                quantidade=quantidade
            )

        return redirect('listar_produtos')

    return render(request, 'dar_baixa.html', {'produto': produto})

def relatorios(request):
    produtos = Produto.objects.all()
    total_itens = produtos.aggregate(Sum('quantidade'))['quantidade__sum'] or 0
    valor_total = sum(p.quantidade * p.preco for p in produtos)

    context = {
        'produtos': produtos,
        'total_itens': total_itens,
        'valor_total': valor_total,
        'nomes': [p.nome for p in produtos],
        'quantidades': [p.quantidade for p in produtos]
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



from estoque.models import Produto, Movimentacao

for p in Produto.objects.all():
    Movimentacao.objects.create(produto=p, tipo='entrada', quantidade=p.quantidade)
