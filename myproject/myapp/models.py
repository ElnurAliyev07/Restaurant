from django.db import models

class Date(models.Model):
    date = models.DateField()

class Table(models.Model):
    number = models.IntegerField(unique=True)
    is_reserved = models.BooleanField(default=False)

class Reservation(models.Model):
    date = models.ForeignKey(Date, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    menu_items = models.ManyToManyField('MenuItem')

class MenuItem(models.Model):
    price = models.DecimalField(max_digits=8, decimal_places=2)  # Assuming a decimal field for pric
    name = models.CharField(max_length=100)
