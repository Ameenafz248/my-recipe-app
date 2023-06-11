# import necessary modules
import os
import django

# set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_project.settings")
django.setup()

# import models
from recipe_app.models import Ingredient

# open text file with ingredients
with open('ingredients.txt', 'r') as file:
    # read each line and create Ingredient object
    for line in file:
        # remove whitespace and newline characters
        line = line.strip()
        # check if ingredient already exists in database
        if not Ingredient.objects.filter(name=line).exists():
            # create new Ingredient object and save to database
            ingredient = Ingredient(name=line)
            ingredient.save()
