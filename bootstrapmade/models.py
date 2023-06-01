from django.db import models

# Create your models here.

class Dishes(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='pics')
    description = models.CharField()
    price = models.IntegerField()
    status = models.BooleanField(default=True)

class MenuCategory(models.Model):
    menu_category = models.CharField(max_length=100)
    status = models.BooleanField(default=True)


class MenuList(models.Model):
    menu_category = models.ForeignKey(MenuCategory, on_delete=models.CASCADE)
    dish = models.ForeignKey(Dishes, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)




