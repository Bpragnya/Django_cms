from django.contrib import admin
from .models import Dishes, MenuList, MenuCategory

# Register your models here.

admin.site.register(Dishes)
admin.site.register(MenuCategory)
admin.site.register(MenuList)

