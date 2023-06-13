
import os
import django

# set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_project.settings")
django.setup()

from recipe_app.models import Ingredient
units = Ingredient.objects.all()

for i in range (0, len(units)):
    units[i].name = units[i].name.lower()
    units[i].save()
