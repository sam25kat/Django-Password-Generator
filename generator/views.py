# generator/views.py
from django.shortcuts import render
import random
import string

def home(request):
    return render(request, 'generator/home.html')

def password(request):
    length = int(request.GET.get('length', 12))
    characters = list(string.ascii_letters + string.digits + string.punctuation)
    generated_password = ''.join(random.choice(characters) for _ in range(length))
    return render(request, 'generator/password.html', {'password': generated_password})
