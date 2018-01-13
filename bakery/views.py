from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth import authenticate, login
from django.views.generic import View
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector
from django.views.generic import ListView

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Recipes, Comment, Profile
from .serializers import RecipeSerializer
from .forms import CommentForm, UserForm




class recipeList(APIView):
    def get(self, request):
        recipes = Recipes.objects.all()
        serializer = RecipeSerializer(recipes, many=True)
        return Response(serializer.data)

    def post(self):
        pass

<<<<<<< HEAD
class UserFormView(View):
    form_class = UserForm
    template_name = 'bakery/registration_form.html'

    # display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # process form data
    def post(self, request):
        form = self.form_class(request.POST)

=======
    
def add_comment_to_recipe(request, pk):
    recipe = get_object_or_404(Recipes, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
>>>>>>> 76a0deaa4f795b2038d14214df758e8d41eb9f8f
        if form.is_valid():
            user = form.save(commit=False)

            #cleaned (normalized) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            #returns User object if credentials are correct
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/')

        return render(request, self.template_name, {'form': form})

#    recipe = get_object_or_404(Recipes, pk=pk)
#    if request.method == "POST":
#        form = CommentForm(request.POST)
#        if form.is_valid():
#            comment = form.save(commit=False)
#            comment.recipe = recipe
#            comment.save()
#            return redirect('recipe_detail', pk=recipe.pk)
#    else:
#        form = CommentForm()
#    return render(request, 'bakery/add_comment_to_recipe.html', {'form': form})

def add_comment_to_recipe(request):
	form = CommentForm(request.POST or None)

	if request.method == "POST":
		if form.is_valid():
			temp = form.save(commit=False)
			parent = form['parent'].value()

			if parent == "": # set a blank path then save it to get an ID
				temp.path = []
				temp.save() # converting ID to int because save() gives a long int ID
				id = int(temp.id)
				temp.path = [id]
			else: # get the parent node
				node = Comment.objects.get(id = parent)
				temp.depth = node.depth + 1
				s = str(node.path)
				temp.path = eval(s)

				#store parents path than apply comment ID
				temp.save()

				id= int(temp.id)
				temp.path.append(id)

			temp.save() # here i have reversed the order


	comment_tree = Comment.objects.all().order_by("-path")

	return render(request, 'recipe_detail.html', locals())



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

<<<<<<< HEAD
def login_page(request):
    recipes = Recipes.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'bakery/registration/login.html', {'recipes': recipes})


def profiles(request):
    profile = Profile
    return render(request, 'bakery/registration/profile.html', {'profile': profile})


def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, _('Your profile was successfully updated!'))
            return redirect('settings:profile')
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'registration/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })
=======
>>>>>>> 76a0deaa4f795b2038d14214df758e8d41eb9f8f
