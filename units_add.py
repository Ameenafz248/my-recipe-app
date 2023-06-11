# import necessary modules
import os
import django

# set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_project.settings")
django.setup()

# import models
from recipe_app.models import Unit
        
with open('units.txt', 'r') as file:
    gen_list = file.readlines()
    list_len = len(gen_list)
    j = 0
    for i in range (0, int(list_len / 2)):
        unit = Unit(name=gen_list[j].strip(), abbreviation=gen_list[j + 1].strip())
        unit.save()
        j = j + 2
    file.close()