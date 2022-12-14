from django.http import HttpResponse
from django.contrib.auth import login
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

# import auth token
from rest_framework.authtoken.models import Token

from .forms import * 
# Create your views here.

login_url = 'login'

def test(request):
    return HttpResponse("Hello World!")

def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)

        if form.is_valid():
            invite = form.cleaned_data.get("invite")
            invite = Invites.objects.get(invite=invite)
            user = form.save()
            login(request, user)
            UserProfile.objects.get_or_create(user=request.user)
            token = Token.objects.get_or_create(user=request.user)
            invite.delete()
            return redirect("profile")

    else:
        form = CreateUserForm()

    return render(request, 'pages/register.html', {'form': form})

@login_required(login_url=login_url)
def editprofile(request):
    UserProfile.objects.get_or_create(user=request.user)
    user_token = Token.objects.get(user=request.user)
    if request.method == "POST":
        form = UserProfileForm(request.POST, request.FILES , instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect("profile")
    else:
        form = UserProfileForm(instance=request.user)
    return render(request, "pages/profile.html", {"form": form, "token": user_token})
