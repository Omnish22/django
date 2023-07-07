from django.shortcuts import render, redirect
from .models import Recipe
from django.contrib.auth.models import User 
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/login/')
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



def register(request):

    if request.method == "POST":
        fName = request.POST.get('firstName')
        lName = request.POST.get('lastName')
        email = request.POST.get('email')
        password = request.POST.get('password')

        print(User.objects.filter(username=email))
        user = User.objects.filter(username=email)
        if user.exists():
            messages.info(request, "User Already Exists")
            return redirect ("/register/")
            
        user = User.objects.create_user(
            username=email,
            password=password,   
        )

        user.first_name=fName
        user.last_name = lName 
        user.save()

        print(User.objects.all())
        messages.info(request, "User Created Successfully")
        return redirect('/register/')

    return render(request, 'vege/register.html')


def login_page(request):
    if request.method == "POST":
        username = request.POST.get('email')
        password = request.POST.get('password')
        
        # CHECK IF USERNAME EXIST IN DATABASE OR NOT 
        if not User.objects.filter(username=username).exists():
            messages.info(request, "Invalid Credentials")
            return redirect('/login/')
        
        # CHECK PASSWORDS
        user = authenticate(username=username, password=password)
        if user is None:
            messages.info(request, "Invalid Credentials")
            return redirect('/login/')
        
        else:
            # CREATING SESSION  
            login(request, user)
            return redirect('/')

    return render(request, 'vege/login.html')


def logout_page(request):
    logout(request)
    return redirect('/login/')