from django.urls import path
from . import views

urlpatterns = [
    # Rota para listar (GET) e criar (POST) produtos
    # Ex: GET /produtos/, POST /produtos/
    path('v1/', views.PadariaList.as_view(), name='padaria_list_create'),
    
    # Rota para ver (GET), editar (PUT) e deletar (DELETE) um produto específico
    # Ex: GET /produtos/1/, PUT /produtos/1/, DELETE /produtos/1/
    path('v1/<int:pk>/', views.PadariaDetail.as_view(), name='padaria_detail_update_delete'),
]