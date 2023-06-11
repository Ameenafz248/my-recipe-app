from django.urls import path
from .views import RecipeListView, RecipeDetailView, UserRecipeListView, voteToggle, RecipeCreateView, RecipeDeleteView
urlpatterns = [
    path("vote/", voteToggle, name="vote_toggle"),
    path("create/", RecipeCreateView.as_view(), name="recipe_create"),
    path("<uuid:pk>", RecipeDetailView.as_view(), name="recipe_detail"),
    path("<uuid:pk>/delete/", RecipeDeleteView.as_view(), name="delete"),
    path("<str:username>/", UserRecipeListView.as_view(), name="user_recipe_list"),
    path("", RecipeListView.as_view(), name="home"),
]

