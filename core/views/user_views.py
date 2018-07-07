from django.shortcuts import render

__author__ = 'andrews'


def registration(request):

    return render(request, 'core/register.html')

def sign_in(request):

    return render(request, 'core/signin.html')

def sign_up(request):

    return render(request, 'core/signup.html')