from core.forms.user_form import SignupsForm, LoginForm
from core.models.signups import Signup
from django.contrib.auth import authenticate, login
from django.shortcuts import render

__author__ = 'andrews'


def registration(request):

    return render(request, 'core/register.html')

def sign_in(request):
    if request.method == 'POST':
        login_form = LoginForm(data=request.POST)
        if login_form.is_valid():
            phone = login_form.cleaned_data['phone']
            password = login_form.cleaned_data['password']

            user = authenticate(request, username=phone, password=password)

            if user is not None:
                try:
                    login(request,user)
                except:
                    pass


    login_form = LoginForm()
    context = {'login_form': login_form}

    return render(request, 'core/signin.html',context)

def sign_up(request):
    if request.method == 'POST':
        signup_form = SignupsForm(data=request.POST)
        if signup_form.is_valid():
            first_name = signup_form.cleaned_data['first_name']
            last_name = signup_form.cleaned_data['last_name']
            email = signup_form.cleaned_data['email']
            phone = signup_form.cleaned_data['phone']

            new_signup=Signup(first_name=first_name,last_name=last_name,email=email,phone=phone)
            new_signup.save()

    signup_form = SignupsForm()
    context = {'signup_form': signup_form}
    return render(request, 'core/signup.html',context)