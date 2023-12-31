from django.contrib import admin
from .forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

CustomUser = get_user_model()

class CustomUserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = CustomUser
    list_display =  [
        "email",
        "username",
        "is_superuser",
    ]
admin.site.register(CustomUser, CustomUserAdmin)

# Register your models here.
