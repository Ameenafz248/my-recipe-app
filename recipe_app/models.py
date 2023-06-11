from django.db import models
from django.conf import settings
from django.urls import reverse
import uuid


class Ingredient(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Unit(models.Model):
    name = models.CharField(max_length=20)
    abbreviation = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    

class Recipe(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length = 25)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    upvotes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="recipes_voted", blank=True)
    tags = models.ManyToManyField(Tag, blank=True, related_name="recipes")
    image = models.ImageField(upload_to="images/")
    ingredients = models.ManyToManyField(Ingredient, through="RecipeIngredient")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("recipe_detail", args=[str(self.id)])


class RecipeIngredient(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="recipeingredients")
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=6, decimal_places=2)


    def __str__(self):
        return f"{self.amount} {self.unit.abbreviation} {self.ingredient.name}"

