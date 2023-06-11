from django.contrib import admin
from .models import Recipe, Ingredient, Tag, Unit, RecipeIngredient

admin.site.register(Recipe)
admin.site.register(Ingredient)
admin.site.register(Tag)
admin.site.register(Unit)
admin.site.register(RecipeIngredient)

# Register your models here.
