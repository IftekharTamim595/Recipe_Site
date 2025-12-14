from django.shortcuts import render, redirect, get_object_or_404
from .models import Recipe

# Create your views here.

def index(request):
    return render(request, 'home/index.html')

def recipe_list(request):
    search_query = request.GET.get('search', '').strip()
    if search_query:
        recipes = Recipe.objects.filter(name__icontains=search_query)
    else:
        recipes = Recipe.objects.all()

    return render(request, 'home/recipe_list.html', {
        'recipes': recipes,
        'search_query': search_query
    })

def add_recipe(request):
    if request.method == "POST":
        name = request.POST.get('recipe_name')
        description = request.POST.get('recipe_description')
        image = request.FILES.get('recipe_image')

        Recipe.objects.create(
            name=name,
            description=description,
            image=image
        )
        return redirect('add_recipe')  # redirect after POST
    
    # GET request: render the add form
    return render(request, 'home/add_recipe.html')


def delete_recipe(request, id):
    obj = get_object_or_404(Recipe, id=id)
    obj.delete()
    return redirect('recipe_list')

def update_recipe(request, id):
    obj = get_object_or_404(Recipe, id=id)

    if request.method == "POST":
        obj.name = request.POST.get('recipe_name')
        obj.description = request.POST.get('recipe_description')

        if request.FILES.get('recipe_image'):
            obj.image = request.FILES['recipe_image']

        obj.save()
        return redirect('recipe_list')

    return render(request, 'home/update_recipe.html', {'sentobj': obj})

        