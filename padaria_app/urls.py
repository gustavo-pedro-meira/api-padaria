from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path("create", views.PadariaCreate.as_view(), name='padaria_create'),
    path('view/<int:pk>', views.PadariaDetail.as_view(), name='padaria_view'),
    path('list', views.PadariaList.as_view(), name='padaria_list'),
    path('edit/<int:pk>', views.PadariaUpdate.as_view(), name='padaria_edit'),
    path('delete/<int:pk>', views.PadariaDelete.as_view(), name='padaria_delete'),
]
 