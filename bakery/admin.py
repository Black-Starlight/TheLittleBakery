from django.contrib import admin
from .models import Recipes, Comment, Profile


admin.site.register(Recipes)
admin.site.register(Comment)
admin.site.register(Profile)
