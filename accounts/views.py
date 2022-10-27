from django.http import HttpResponse
from django.contrib.auth import login
from django.shortcuts import render, redirect, get_object_or_404

from .forms import * 
# Create your views here.
def test(request):
    return HttpResponse("Hello World!")

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            UserProfile.objects.get_or_create(user=request.user)
            return redirect('home')
    else:
        form = UserCreationForm()

    return render(request, 'pages/register.html', {'form': form})



