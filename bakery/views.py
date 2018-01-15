from django.shortcuts import render, get_object_or_404, redirect, render_to_response, HttpResponse
from django.utils import timezone
from django.contrib.auth import authenticate, login
from django.views.generic import View
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector
from django.views.generic import ListView
from django.template import RequestContext
from django.utils.translation import gettext as _

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from django.utils.translation import gettext as _

from .models import Recipes, Comments, Profile, ProfileComments
from django.contrib.auth.models import User
from .serializers import RecipeSerializer
from .forms import CommentForm, UserForm, addRecipeForm, ProfileForm, ProfileCommentsForm




class recipeList(APIView):
    def get(self, request):
        recipes = Recipes.objects.all()
        serializer = RecipeSerializer(recipes, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RecipeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
                    return render(request, 'bakery/index.html', )

        return render(request, self.template_name, {'form': form})

def index(request):
    recipes = Recipes.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'bakery/index.html', {'recipes': recipes, 'profile': Profile})

def users(request):
    users = User.objects.all()
    return render(request, 'bakery/users.html', {'users': users, 'profile': Profile})


def users(request):
    users = User.objects.all()
    return render(request, 'bakery/users.html', {'users': users, 'profile': Profile})


def cakes(request):
    recipes = Recipes.objects.filter(bakeType = 'CAKES').order_by('created_date')

    if '' in request.session:
       request.session['p'] = request.session['p'] + 1
    else:
       request.session['p'] = 1

    return render(request, 'bakery/cakes_cupcakes.html', {'recipes': recipes, 'profile': Profile})

def pies(request):
    recipes = Recipes.objects.filter(bakeType = 'PIES').order_by('created_date')
    return render(request, 'bakery/pies.html', {'recipes': recipes, 'profile': Profile})

def cookies(request):
    recipes = Recipes.objects.filter(bakeType = 'COOKIES').order_by('created_date')
    return render(request, 'bakery/cookies.html', {'recipes': recipes, 'profile': Profile})

def bakedGoods(request):
    recipes = Recipes.objects.filter(bakeType = 'OTHER').order_by('created_date')
    return render(request, 'bakery/baked-goods.html', {'recipes': recipes, 'profile': Profile})

def liked_list(request):
    recipes = Recipes.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'bakery/liked_list.html', {'recipes': recipes, 'profile': Profile})

def recipe_list(request):
    recipes = Recipes.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'bakery/recipe_list.html', {'recipes': recipes, 'profile': Profile})

def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipes, pk=pk)
    form = CommentForm(request.POST or None)
    recipe = get_object_or_404(Recipe, pk=pk)

	if request.method == "POST":
		if form.is_valid():
			temp = form.save(commit=False)
			parent = form['parent'].value()
			form.commenter = request.user
			form.recipe = recipe

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
	return render(request, 'bakery/recipe_detail.html', {'recipes': recipe, 'profile': Profile, 'commentForm': form})
    

def login_page(request):
    recipes = Recipes.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'bakery/registration/login.html', {'recipes': recipes, 'profile': Profile})


def add_recipe(request):
    form = addRecipeForm()
    return render(request, 'bakery/add_recipe.html', {'form': form})




def favorite(request, username):
    return render(request, 'bakery/favorite.html', { 'profile': Profile})

def made(request, username):
    return render(request, 'bakery/made.html', { 'profile': Profile})

def friends(request, username):
    return render(request, 'bakery/friends.html', {'profile': Profile})

def get_user_profile(request, username):
    user = User.objects.get(username=username)
    profile = Profile
    if request.method == "POST":
        form = ProfileCommentsForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.commenter = request.user
            comment.profile = user.profile
            comment.save()
            return redirect('userProfile', username)
    else:
        form = ProfileCommentsForm()
    return render(request, 'bakery/user_profile.html', {"user":user, 'profile': Profile, 'comments_form': form, "comments" : ProfileComments})

def update_profile(request, username):
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if  profile_form.is_valid():
            profile_form.save()
            messages.success(request, _('Your profile was successfully updated!'))
            return redirect('userProfile', username)
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'bakery/profile-edit.html', {
        'profile_form': profile_form
    })

def liked(request, pk):
    return HttpResponse('entered text:' + request.POST[pk])
    if request.method == 'POST':
        Profile.favs = Profile.favs + recipes
        return redirect('cakes_cupcakes');




def search(request):
    query = request.GET.get('q')
    try:
        query = int(query)
    except ValueError:
        query = None
        results = None
    if query:
        results = Recipes.objects.get(uid=query)
    context = RequestContext(request)
    return render_to_response('results.html', {"results": results,}, context_instance=context)
