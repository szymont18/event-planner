from django.contrib import admin
from .models import WebsiteUser


# Register your models here.


class WebstieUserAdmin(admin.ModelAdmin):
    list_display = ("username",)


admin.site.register(WebsiteUser, WebstieUserAdmin)
