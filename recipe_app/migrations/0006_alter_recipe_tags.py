# Generated by Django 4.2 on 2023-05-08 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_app', '0005_alter_recipe_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='tags',
            field=models.ManyToManyField(null=True, to='recipe_app.tag'),
        ),
    ]