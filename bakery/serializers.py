from rest_framework import serializers
from .models import Recipes, Profile

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipes
        fields = ('pk','imageDir','caption','title', 'serve', 'prepTime', 'cookTime', 'kcal', 'fat', 'carbs', 'sugar', 'protein', 'salt', 'ingredients', 'recipe')

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('user','bio', 'location', 'birth_date', 'favs', 'made','friends')
