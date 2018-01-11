from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Recipes
from .serializers import RecipeSerializer
from .forms import CommentForm

class recipeList(APIView):
    def get(self, request):
        recipes = Recipes.objects.all()
        serializer = RecipeSerializer(recipes, many=True)
        return Response(serializer.data)

    def post(self):
        pass

    
def add_comment_to_recipe(request, pk):
    recipe = get_object_or_404(Recipes, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.recipe = recipe
            comment.save()
            return redirect('recipe_detail', pk=recipe.pk)
    else:
        form = CommentForm()
    return render(request, 'bakery/add_comment_to_recipe.html', {'form': form})

def index(request):
    recipes = Recipes.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'bakery/index.html', {'recipes': recipes})

def cakes(request):
    recipes = Recipes.objects.filter(bakeType = 'CAKES').order_by('created_date')

    if '' in request.session:
       request.session['p'] = request.session['p'] + 1
    else:
       request.session['p'] = 1

    return render(request, 'bakery/cakes_cupcakes.html', {'recipes': recipes})

def pies(request):
    recipes = Recipes.objects.filter(bakeType = 'PIES').order_by('created_date')
    return render(request, 'bakery/pies.html', {'recipes': recipes})

def cookies(request):
    recipes = Recipes.objects.filter(bakeType = 'COOKIES').order_by('created_date')
    return render(request, 'bakery/cookies.html', {'recipes': recipes})

def bakedGoods(request):
    recipes = Recipes.objects.filter(bakeType = 'OTHER').order_by('created_date')
    return render(request, 'bakery/baked-goods.html', {'recipes': recipes})

def liked_list(request):
    recipes = Recipes.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'bakery/liked_list.html', {'recipes': recipes})

def recipe_list(request):
    recipes = Recipes.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'bakery/recipe_list.html', {'recipes': recipes})

def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipes, pk=pk)
    return render(request, 'bakery/recipe_detail.html', {'recipe': recipe})

