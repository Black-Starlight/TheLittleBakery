from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from bakery import views


urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^recipe_list$', views.cakes, name='recipe_list'),
    url(r'^cakes_cupcakes$', views.cakes, name='cakes_cupcakes'),
    url(r'^pies$', views.pies, name='pies'),
    url(r'^cookies$', views.cookies, name='cookies'),
    url(r'^baked-goods$', views.bakedGoods, name='baked-goods'),
    url(r'^liked_list$', views.liked_list, name='liked_list'),
    url(r'^post/(?P<pk>\d+)/$', views.recipe_detail, name='recipe_detail'),
    url(r'^recipes/', views.recipeList.as_view()),
    url(r'^tweets.(?P<pk>[0-9]+)$', views.recipeList.as_view()),
    url(r'^registration_form$', views.registration_form, name='registration_form'),
    url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_recipe, name='add_comment_to_recipe')
]
