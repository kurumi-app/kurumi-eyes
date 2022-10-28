from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
# Create your views here.

login_url = 'login'

def home(request):
    return render(request, 'pages/home.html')

@login_required(login_url=login_url)
def dashboard(request):
    context = {
        'users': get_user_model().objects.count(),
    }
    return render(request, 'pages/dashboard.html', context)

