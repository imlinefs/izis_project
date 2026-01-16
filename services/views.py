from django.shortcuts import render
from .models import Service  

# Criar a função service_list para pegar os dados do banco de dados e mostrar no HTML

def service_list(request):
    # Busca todos os serviços no banco de dados
    services = Service.objects.all()
    # Manda os dados para um arquivo HTML
    return render(request, 'services/list.html', {'services': services})