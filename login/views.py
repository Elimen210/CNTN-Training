from django.contrib.auth.forms import UsernameField
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as auth_login, logout
from .forms import SignupForm, LoginForm
from landing.models import UserProfile

class index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'login/index.html')



def loginView(request):
    if request.method == 'POST':
        login_form = LoginForm(request, data=request.POST)

        if login_form.is_valid():
            user = login_form.get_user()
            auth_login(request, user)
            return redirect('landing')
    else:
        login_form = LoginForm()

    return render(request, 'login/index.html', {'login_form': login_form})


def signupView(request):
    if request.method == 'POST':
        signup_form = SignupForm(data=request.POST)
        if signup_form.is_valid():
            user = signup_form.save(commit=False)
            username = signup_form.cleaned_data['username']
            password = signup_form.cleaned_data['password']
            user.set_password(password)
            user = signup_form.save()
            
            user.save()

            UserProfile.objects.create(user=user, name=username)

            auth_login(request, user)
            return redirect('landing')
    else:
        signup_form = SignupForm()

    context = {
        'signup_form': signup_form,
    }
    return render(request, 'login/index.html', context)

def logout_view(request):
        logout(request)
        return redirect('login-home')