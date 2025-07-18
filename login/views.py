from django.contrib.auth.forms import UsernameField
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth import logout as django_logout
from .forms import SignupForm, LoginForm

class index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'login/index.html')

def loginView(request):
    login_form = LoginForm(data=request.POST)
    signup_form = SignupForm(data=request.POST)

    if login_form.is_valid():
        login_form = LoginForm(data=request.POST)
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate (
            request,
            username=username,
            password=password,
                )

        if user is not None:
            auth_login(request, user)
            return redirect('landing')

    return render(request, 'login/index.html', {
        'login_form': login_form,
        })

def signupView(request):
    signup_form = SignupForm(data=request.POST)

    if request.method == 'POST':
        if signup_form.is_valid():
            user = signup_form.save(commit=False)
            username = signup_form.save(['username'])
            password = signup_form.save(['password'])
            user.save()

            user = [
                ['username'], ['password'],
            ]

            return redirect('landing')

    return render(request, 'login/index.html', {
        'signup_form': signup_form,
        })

def logout_view(request):
        logout(request)
        return redirect('login-home')