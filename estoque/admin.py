from django.contrib import admin
from .models import Produto

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'quantidade', 'preco') 
    search_fields = ('nome',)                      
    list_filter = ('quantidade',)          
