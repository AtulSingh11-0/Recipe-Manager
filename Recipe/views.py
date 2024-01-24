from django.shortcuts import redirect, render
from django.http import HttpResponse
from Recipe.models import Recipe

# Create your views here.

# route for /recipe
# Creating/Posting the Recipe
def recipeForm(request):
  
  if request.method == "POST":
    data = request.POST
    
    recipe_name = data.get('recipe_name')
    recipe_description = data.get('recipe_description')
    recipe_image = request.FILES.get('recipe_image')
    
    Recipe.objects.create(
      recipe_name = recipe_name, 
      recipe_description = recipe_description, 
      recipe_image = recipe_image
    )
    
    print(
      recipe_name, 
      recipe_description, 
      recipe_image, 
    )
    
    return redirect('/recipe/')
  
  context={'page': 'Recipe Register'}
  return render(request, 'recipeForm.html', context)


# Reading/Getting the Recipe
def recipes(requset):
  
  queryset = Recipe.objects.all()
  searchItem = requset.GET.get('search_recipe')
  
  if(searchItem):
    queryset = queryset.filter(recipe_name__icontains = searchItem)
  
  context = {'recipes':queryset, 'page':'Recipes'}
  return render(requset, "recipes.html", context=context)


# Updating the Recipe
def updateRecipe(request, id):
  
  queryset = Recipe.objects.get(id=id)
  
  if request.method == "POST":
    data = request.POST
    
    recipe_name = data.get('recipe_name')
    recipe_description = data.get('recipe_description')
    recipe_image = request.FILES.get('recipe_image')
    
    queryset.recipe_name = recipe_name
    queryset.recipe_description = recipe_description
    if(recipe_image):
      queryset.recipe_image = recipe_image  
    
    print(
      recipe_name, 
      recipe_description, 
      recipe_image, 
    )
    
    queryset.save()
    
    return redirect('/recipes/')
  
  context = {'recipe': queryset, 'page':'Update Recipe'}
  
  return render(request, 'updateRecipe.html', context)


# Deleting the Recipe
def deleteRecipe(request, id):
  
  Recipe.objects.filter(id=id).delete()
  return redirect('/recipes/')