from django.contrib import admin
from .models import Recipes, Comment, Profile, ProfileComments


admin.site.register(Recipes)
admin.site.register(Comment)
admin.site.register(Profile)
admin.site.register(ProfileComments)
