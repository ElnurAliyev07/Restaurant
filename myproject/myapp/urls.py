from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('about/', views.about, name='about'),
    path('logout/', views.logout, name='logout'),
    path('select_date/', views.select_date, name='select_date'),
    path('select_table/<int:date_id>/', views.select_table, name='select_table'),
    path('select_menu_items/<int:date_id>/<int:table_number>/', views.select_menu_items, name='select_menu_items'),
    path('confirm_reservation/<int:date_id>/<int:table_number>/', views.confirm_reservation, name='confirm_reservation'),
]

