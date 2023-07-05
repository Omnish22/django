from django.shortcuts import render, redirect
from .models import Recipe

# Create your views here.

def recipes(request):
    # CHECKING IF REQUEST COMING IS POST OR GET
    if request.method=='POST':
        
        # EXTRACTING DATA FROM REQUEST
        data = request.POST
        name = data.get('recipe_name')
        description = data.get("recipe_description")
        # EXTRACTING IMAGE FILE FROM REQUEST IS BIT DIFFERENT
        file = request.FILES.get('recipe_image')

        # CREATING DATA INTO DATABASE
        Recipe.objects.create(
            recipe_name=name,
            recipe_description=description,
            recipe_image = file
        )

        return redirect("/")

    data = Recipe.objects.all()
    context = {'data':data}
    return render(request, "vege/recipes.html", context=context)


def delete(request, id):
    recipe = Recipe.objects.filter(id=id)
    if len(recipe)>0:
        recipe.delete()
    return redirect("/")

def update(request, id):

    recipe = Recipe.objects.get(id=id)
    if request.method=="POST":
        updated_data = request.POST
        updated_name = updated_data.get('recipe_name')
        updated_description = updated_data.get('recipe_description')
        recipe_img = request.FILES.get('recipe_image')

        recipe.recipe_name = updated_name
        recipe.recipe_description = updated_description
        if recipe_img:
            recipe.recipe_image = recipe_img

        recipe.save()
        return redirect("/")

    
    return render(request, 'vege/update.html', context={"recipe":recipe})