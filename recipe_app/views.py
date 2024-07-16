from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .models import Receipe
from .forms import RecipeForm


# Create your views here.
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

# Confirm deletion view
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

# return render(request, 'confirm_delete.html', {'recipe': recipe})

'''
def receipes(request):
    print("recipes view called..")
    if request.method == "POST":
        data = request.POST
        print(data)
        receipe_image = request.FILES.get('receipe_image')
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')
        print(receipe_description)
        print(receipe_name)
        print(receipe_image)
    return render(request, 'recipes/receipes.html')

def add_recipe(request):
    if request.method == 'POST':
        print(request.POST)
        print(request.FILES)
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success_page')
    else:
        form = RecipeForm()
    return render(request, 'recipes/receipes.html', {'form': form})

1.
POST success output:
[12/Jul/2024 22:04:49] "GET /receipes/contact/ HTTP/1.1" 200 598
recipes view called..
<QueryDict: {}>
[12/Jul/2024 22:04:52] "GET /receipes/ HTTP/1.1" 200 1616
recipes view called..
<QueryDict: {}>
[12/Jul/2024 22:06:06] "GET /receipes/ HTTP/1.1" 200 1542
2.
recipes view called..
[13/Jul/2024 13:13:28] "GET /receipes/ HTTP/1.1" 200 1542
recipes view called..
<QueryDict: {'csrfmiddlewaretoken': ['QH1KsziVkfWSwA6e6dCgdkVxYV5TeJpyGOqRDeixyO5yooIe3r83xHS4K4nYI9HT'], 'recipe_name': ['Mutton'], 'recipe_description': ['Gravy'], 'recipe_image': ['']}>
None
None
[13/Jul/2024 13:13:46] "POST /receipes/ HTTP/1.1" 200 1542
success!
3. Final..
recipes view called..
[13/Jul/2024 15:27:09] "GET /receipes/ HTTP/1.1" 200 1528
<QueryDict: {'csrfmiddlewaretoken': ['wp5K3Borku8KtUHKeIFb8ZUenhCHPKk1mwuRego3y3hqlIjKbWbYsmRL9qUMjaCm'], 'receipe_name': ['Butter Paneer'], 'receipe_description': ['Medium spicy semi gravy dish']}>
<MultiValueDict: {'receipe_image': [<InMemoryUploadedFile: IMG_20240703_143326.jpg (image/jpeg)>]}>
[13/Jul/2024 15:27:54] "POST /receipes/add_recipe/ HTTP/1.1" 302 0
[13/Jul/2024 15:27:54] "GET /receipes/success-page/ HTTP/1.1" 200 1107
[13/Jul/2024 15:28:04] "GET /receipes/about/ HTTP/1.1" 200 1133
recipes view called..
[13/Jul/2024 15:28:05] "GET /receipes/ HTTP/1.1" 200 1528
'''