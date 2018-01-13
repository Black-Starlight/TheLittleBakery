from rest_framework import serializers
from .models import Recipes

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipes
        fields = ('pk','title', 'serve', 'prepTime', 'cookTime', 'kcal', 'fat', 'carbs', 'sugar', 'protein', 'salt', 'ingredients', 'recipe')
