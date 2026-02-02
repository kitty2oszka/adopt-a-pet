from django.shortcuts import render
from .models import Pet
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect 
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404

def pet_list(request):
    search_query = request.GET.get('q')
    category = request.GET.get('category')
    
    pets = Pet.objects.all()

    if category:
        pets = pets.filter(species=category)
    if search_query:
        pets = pets.filter(name__icontains=search_query)    

    
    return render(request, 'pet_list.html', {'pets': pets})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login') 
    else:
        form = UserCreationForm()
    
    return render(request, 'registration/register.html', {'form': form})

def pet_detail(request, pk):
    #pk to Primary Key obiektu Pet
    pet = get_object_or_404(Pet, pk=pk)
    return render(request, 'pet_details.html', {'pet': pet})