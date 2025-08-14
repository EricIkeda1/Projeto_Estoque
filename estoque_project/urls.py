from django.contrib import admin
from django.urls import path
from estoque import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.listar_produtos, name='listar_produtos'),
    path('admin/', admin.site.urls),
    path('cadastrar/', views.cadastrar_produto, name='cadastrar_produto'),
    path('listar/', views.listar_produtos, name='listar_produtos'),
    path('movimentacoes/', views.movimentacoes, name='movimentacoes'),
    path('relatorios/', views.relatorios, name='relatorios'),
]
