from django.contrib import admin
from micameo.enroll.models import Enroll


# Register your models here.
@admin.register(Enroll)
class Enroll(admin.ModelAdmin):
    list_display = ["full_name", "username", "phone_number", "where_find_you", "followers"]
    search_fields = ["full_name"]
