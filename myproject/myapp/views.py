from django.shortcuts import render, redirect, HttpResponse

def home(request):
    return render(request, 'home.html')

from django.shortcuts import render, get_object_or_404, redirect
from .models import Date, Table, Reservation, MenuItem

def select_date(request):
    dates = Date.objects.all()
    return render(request, 'select_date.html', {'dates': dates})

def select_table(request, date_id):
    print(f"Received date_id: {date_id}")
    date = get_object_or_404(Date, pk=date_id)
    tables = Table.objects.filter(is_reserved=False)
    return render(request, 'select_table.html', {'date': date, 'tables': tables})

def select_menu_items(request, date_id, table_number):
    date = get_object_or_404(Date, pk=date_id)
    table = get_object_or_404(Table, number=table_number, is_reserved=False)
    menu_items = MenuItem.objects.all()
    return render(request, 'select_menu_items.html', {'date': date, 'table': table, 'menu_items': menu_items})

from django.shortcuts import render, get_object_or_404
from .models import Date, Table, MenuItem

def confirm_reservation(request, date_id, table_number):
    date = get_object_or_404(Date, pk=date_id)
    table = get_object_or_404(Table, number=table_number)
    menu_items = MenuItem.objects.all()

    selected_menu_item_ids = request.POST.getlist('menu_items')

    selected_menu_items = menu_items.filter(id__in=selected_menu_item_ids)

    total_price = sum(item.price for item in selected_menu_items)

    return render(request, 'confirm_reservation.html', {'date': date, 'table': table, 'selected_menu_items': selected_menu_items, 'total_price': total_price})


from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required(login_url="login")
def HomePage(request):
    return render(request, "home.html")


from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login

@csrf_protect
def signup(request):
    if request.method == "POST":
        uname = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')

        if uname and password and repeat_password:
            if password == repeat_password:
                if not User.objects.filter(username=uname).exists():
                    my_user = User.objects.create_user(uname, email, password)
                    my_user.save()
                    messages.success(request, "Signup Successfully!!!")
                    return redirect("login")
                else:
                    messages.info(request, "Username is already taken")
            else:
                messages.info(request, "Passwords do not match")
        else:
            messages.info(request, "All fields must be filled")

    return render(request, "signup.html")

@csrf_protect
def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, 'login.html')


def about(request):
    return render(request, 'about.html')
def logout(request):
    return render(request, 'home.html')