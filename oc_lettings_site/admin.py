from django.contrib import admin
from django.contrib.admin.sites import AdminSite
from .models import Letting, Address, Profile


class MyAdminSite(AdminSite):
    class Media:
        css = {
            'all': ('css/dark_theme.css',)
        }


admin.site = MyAdminSite()

admin.site.register(Letting)
admin.site.register(Address)
admin.site.register(Profile)