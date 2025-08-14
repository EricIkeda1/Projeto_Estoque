from django.contrib import admin
from django.urls import path
from estoque import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Páginas protegidas
    path('', views.listar_produtos, name='listar_produtos'),
    path('cadastrar/', views.cadastrar_produto, name='cadastrar_produto'),
    path('movimentacoes/', views.movimentacoes, name='movimentacoes'),
    path('relatorios/', views.relatorios, name='relatorios'),
    path('painel-estoque/', views.painel_estoque, name='painel_estoque'),

    # Login / Logout
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # Recuperação de senha
    path(
        'password_reset/',
        auth_views.PasswordResetView.as_view(
            template_name='registration/password_reset_form.html'
        ),
        name='password_reset'
    ),
    path(
        'password_reset_done/',
        auth_views.PasswordResetDoneView.as_view(
            template_name='registration/password_reset_done.html'
        ),
        name='password_reset_done'
    ),
    path(
        'reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(
            template_name='registration/password_reset_confirm.html'
        ),
        name='password_reset_confirm'
    ),
    path(
        'reset/done/',
        auth_views.PasswordResetCompleteView.as_view(
            template_name='registration/password_reset_complete.html'
        ),
        name='password_reset_complete'
    ),
]
