from django.shortcuts import render

# Create your views here.

from .utils import get_consultancy_services

def services_view(request):
    services = get_consultancy_services()
    
    context = {
        'services': services,
        'has_error': services is None,
    }
    return render(request, context)