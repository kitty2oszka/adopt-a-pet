from django.shortcuts import render
from .models import Pet


def pet_list(request):
    category = request.GET.get('category')
    
    if category:
        pets = Pet.objects.filter(species=category)
    else:
        pets = Pet.objects.all()
    
    return render(request, 'pet_list.html', {'pets': pets})