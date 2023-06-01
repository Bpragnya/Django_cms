from django.shortcuts import render
from .models import MenuCategory, MenuList, Dishes

# Create your views here.
def index(request):

    menu_ctgs = MenuCategory.objects.all()
    menu_lists = MenuList.objects.all()
    dishes = Dishes.objects.all()


    return render(request, 'index.html', {'menu_ctgs':menu_ctgs, 'menu_lists': menu_lists, 'dishes': dishes})
