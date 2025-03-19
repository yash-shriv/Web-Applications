from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .models import Receipe
from .forms import RecipeForm

def homepage(request):
    return render(request, 'homepage.html')

@login_required
def receipes(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/receipes/')
    else:
        form = RecipeForm()
    search_query = request.GET.get('search', '')
    queryset = Receipe.objects.filter(
        Q(receipe_name__icontains=search_query) |
        Q(receipe_description__icontains=search_query)
    ).distinct()
    context = {
        'form': form,
        'receipes': queryset,
        'search_query': search_query,
    }    
    return render(request, 'recipes/receipes.html', context)

def contact(request):
    return render(request, 'recipes/contact.html')

def about(request):
    return render(request, 'recipes/about.html')

def success_page(request):
    return render(request, 'recipes/success_page.html')

def confirm_delete_recipe(request, recipe_id):
    recipe = get_object_or_404(Receipe, id=recipe_id)
    if request.method == 'POST':
        recipe.delete()
        return redirect('receipes')
    return render(request, 'confirm_delete.html', {'recipe': recipe})

@login_required
def delete_recipe(request, id):
    recipe = get_object_or_404(Receipe, id=id)
    if request.method == 'POST':
        recipe.delete()
        return redirect('receipes')
    return render(request, 'recipes/confirm_delete.html', {'recipe': recipe})

@login_required
def edit_recipe(request, recipe_id):
    recipe = get_object_or_404(Receipe, id=recipe_id)
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('receipes')
    else:
        form = RecipeForm(instance=recipe)
    
    context = {
        'form': form,
        'recipe': recipe,
    }
    return render(request, 'recipes/edit_recipe.html', context)
