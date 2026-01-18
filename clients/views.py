from django.shortcuts import render
from .models import Cliente

def client_list(request):
    # Busca todas as clientes cadastradas
    clients = Cliente.objects.all()
    
    # Envia para o HTML
    return render(request, 'clients/list.html', {'clients': clients})