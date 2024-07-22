from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User


def login_view(request):
    if request.method == 'POST':
        login_form = AuthenticationForm(request, data=request.POST)
        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'login.html', context={"message": "Password yoki Username xato"})

    return render(request, 'login.html')


def regester_view(request):
    if request.method == 'POST':
        first_name = request.POST['name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        password1 = request.POST['password1']
        if password != password1:
            return render(request, 'regester.html', context={"message_password": "Error Password!!!"})
        elif User.objects.filter(username=username).exists():
                return render(request, 'regester.html', context={"message": "Bunday usernamelik foydalanuvchi mavjud!!"})
        else:
            if first_name and last_name and username and password and password1:

                new_user = User(first_name=first_name, last_name=last_name, email=email, username=username)
                new_user.set_password(password)
                new_user.save()
                return redirect('login')
            else:
                return render(request, 'regester.html',{'message_com': "Error have empty place!!!"})

    return render(request, 'regester.html')


def account(request):
    return render(request, 'account.html')


def log_out_view(request):
    logout(request)
    return redirect('index')
