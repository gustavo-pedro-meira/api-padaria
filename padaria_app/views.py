# seu_app/views.py

import json
from django.http import JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.forms.models import model_to_dict

from .models import Padaria

# Um "Mixin" para evitar repetir código.
# Este decorator desativa a proteção CSRF. Essencial para APIs stateless.
# Use com cautela e considere outros métodos de autenticação (ex: tokens) em produção.
@method_decorator(csrf_exempt, name='dispatch')
class JsonView(View):
    """
    View base que desativa CSRF e prepara para respostas JSON.
    """
    def json_response(self, data, status=200):
        """Helper para criar uma resposta JSON padronizada."""
        return JsonResponse(data, status=status, safe=False, json_dumps_params={'ensure_ascii': False})

class PadariaList(JsonView):
    """
    View para listar todos os produtos ou criar um novo.
    - GET: Retorna a lista de todos os produtos.
    - POST: Cria um novo produto a partir de um corpo JSON.
    """
    def get(self, request, *args, **kwargs):
        # Pega todos os objetos, converte para uma lista de dicionários
        produtos = list(Padaria.objects.values())
        return self.json_response(produtos)

    def post(self, request, *args, **kwargs):
        try:
            # Carrega os dados do corpo da requisição JSON
            data = json.loads(request.body)
            # Cria o novo produto no banco de dados
            produto = Padaria.objects.create(**data)
            # Retorna o produto recém-criado com status 201 (Created)
            return self.json_response(model_to_dict(produto), status=201)
        except (json.JSONDecodeError, TypeError) as e:
            return self.json_response({'erro': 'JSON inválido ou mal formatado'}, status=400)

class PadariaDetail(JsonView):
    """
    View para detalhar, atualizar ou deletar um produto específico.
    - GET: Retorna os detalhes de um produto.
    - PUT: Atualiza um produto existente.
    - DELETE: Deleta um produto.
    """
    def get(self, request, pk, *args, **kwargs):
        # Busca o objeto pelo ID (pk) ou retorna 404 se não encontrar
        produto = get_object_or_404(Padaria, pk=pk)
        # Converte o objeto para um dicionário e retorna como JSON
        return self.json_response(model_to_dict(produto))

    def put(self, request, pk, *args, **kwargs):
        produto = get_object_or_404(Padaria, pk=pk)
        try:
            data = json.loads(request.body)
            # Atualiza os campos do objeto com os dados recebidos
            for key, value in data.items():
                setattr(produto, key, value)
            produto.save()
            return self.json_response(model_to_dict(produto))
        except (json.JSONDecodeError, TypeError):
            return self.json_response({'erro': 'JSON inválido ou mal formatado'}, status=400)

    def delete(self, request, pk, *args, **kwargs):
        produto = get_object_or_404(Padaria, pk=pk)
        produto.delete()
        # Retorna uma resposta vazia com status 204 (No Content), indicando sucesso
        return HttpResponse(status=204)