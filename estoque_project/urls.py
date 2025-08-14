from django.contrib import admin
from django.urls import path
from estoque import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.listar_produtos, name='listar_produtos'),
    path('cadastrar/', views.cadastrar_produto, name='cadastrar_produto'),
    path('movimentacoes/', views.movimentacoes, name='movimentacoes'),
    path('relatorios/', views.relatorios, name='relatorios'),
]
