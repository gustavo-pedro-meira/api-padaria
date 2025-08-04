from django.urls import path
from padaria_app.views import home

urlpatterns = [
    path('', home),

]
 