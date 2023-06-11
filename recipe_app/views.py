import json
from typing import Any, Dict
from django.db.models import Count  
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Recipe, RecipeIngredient, Unit, Ingredient, Tag
from django.contrib.auth import get_user_model
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.views.decorators.http import require_POST
from django.urls import reverse_lazy


class UserRecipeListView(ListView, LoginRequiredMixin):
    model = Recipe
    template_name = "user_recipe_list.html"
    slug_url_kwarg = "username"

    def get_queryset(self):
        User = get_user_model()
        user = User.objects.get(username=self.kwargs.get("username"))
        if (user):
            queryset = Recipe.objects.annotate(count=Count('upvotes')).order_by('-count').filter(author=user)
            return queryset
        else:    
            response = render(self.request, "404.html")
            response.status_code = 404
            return response
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        User = get_user_model()
        user = User.objects.get(username=self.kwargs.get("username"))
        if (user):
            context['recipe_user'] = user
        return context


class RecipeListView(ListView):
    model = Recipe
    template_name = "home.html"

    def get_queryset(self):
        queryset = Recipe.objects.annotate(count=Count('upvotes')).order_by('-count').select_related('author').prefetch_related('upvotes', 'tags')
        return queryset
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = Tag.objects.annotate(tCount=Count('recipes')).order_by('-tCount')
        return context

class RecipeDetailView(DetailView):
    model = Recipe
    template_name = "recipe_detail.html"

def voteToggle(request):
    if request.method == 'POST':
        User = get_user_model()
        user = User.objects.get(username=request.POST.get('username'))
        if (user is not None):
            recipe = Recipe.objects.get(id=request.POST.get('id'))
            if (recipe is not None):
                if (request.POST.get('op') == 'unlike'):
                    recipe.upvotes.remove(user)
                    return JsonResponse({'flag' : 0})
                else:
                    recipe.upvotes.add(user)
                    return JsonResponse({'flag' : 1})
            return JsonResponse(status=200)
    return JsonResponse({'message': 'error'})


class RecipeCreateView(CreateView):
    model = Recipe
    template_name = "recipe_create.html"
    fields = ('name', 'description', 'image')

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['units'] = Unit.objects.all()
        context['ingredients'] = Ingredient.objects.all()
        context['tags'] = Tag.objects.all()
        return context

    def form_invalid(self, form):
        Tag.objects.create(name="nwTag")
        return super().form_invalid(form)

    def form_valid(self, form):
        form.instance.author = self.request.user
        self.object = form.save()
        arr = form.data.get('ing')
        arr = json.loads(arr)
        recipe = self.object; 
        for ing in arr:
            ingredient = Ingredient.objects.get_or_create(name=ing['ingredient'])
            unit = Unit.objects.get(name=ing['unit'])
            if (unit is None):
                unit = Unit.objects.create(name=ing['unit'], abbreviation=ing['unit'][:3])
            amount = ing['amount']
            RecipeIngredient.objects.create(ingredient=ingredient[0], recipe=recipe, unit=unit, amount=amount)
        arr = form.data.get('ta')
        arr = json.loads(arr)
        for tagTemp in arr:
            tag = Tag.objects.get_or_create(name=tagTemp['tagname'])
            recipe.tags.add(tag[0])
        return HttpResponseRedirect(self.get_success_url()) 

class RecipeDeleteView(DeleteView):
    model = Recipe
    template_name = "recipe_delete.html"
    success_url = reverse_lazy("home")