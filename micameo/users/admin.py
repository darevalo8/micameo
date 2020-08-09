from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model

from micameo.users.forms import UserChangeForm, UserCreationForm
from micameo.users.models import Talent, Client, Category, SubCategory

User = get_user_model()

admin.site.register(Talent)
admin.site.register(Client)
admin.site.register(Category)
admin.site.register(SubCategory)


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    # fieldsets = (("User", {"fields": ("first_name",)}),) + auth_admin.UserAdmin.fieldsets
    list_display = ["username", "first_name", "is_superuser"]
    search_fields = ["email"]
