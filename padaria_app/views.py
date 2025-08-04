from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Padaria

# Create your views here.
def home(request):
    return render(request, 'padaria/home.html')

class PadariaList(ListView):
    model = Padaria
    
class PadariaDetail(DetailView):
    model = Padaria

class PadariaCreate(CreateView):
    model = Padaria
    fields = ["nome", "quantidade", "preco"]
    success_url = reverse_lazy("padaria_list")
    
class PadariaUpdate(UpdateView):
    model = Padaria
    fields = ["nome", "quantidade", "preco"]
    success_url = reverse_lazy("padaria_list")
    
class PadariaDelete(DeleteView):
    model = Padaria
    success_url = reverse_lazy("padaria_list")