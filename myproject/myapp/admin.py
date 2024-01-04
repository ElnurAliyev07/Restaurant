from django.contrib import admin
from .models import Date, Table, Reservation, MenuItem

@admin.register(Date)
class DateAdmin(admin.ModelAdmin):
    list_display = ('date',)

@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ('number', 'is_reserved',)
    list_filter = ('is_reserved',)

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('date', 'table',)
    list_filter = ('date', 'table',)

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')  # Include the 'price' field in the list_display
