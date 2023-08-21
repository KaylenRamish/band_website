
from django.shortcuts import render

def home(request):
    # Your home view logic
    return render(request, 'home.html')

def signup(request):
    # Your signup view logic
    return render(request, 'signup.html')
