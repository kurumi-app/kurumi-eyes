from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .forms import *
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


def upload(request):

    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            ImageUpload = form.save(commit=False)
            ImageUpload.user = request.user 
            ImageUpload.save()
            return redirect('dashboard')
    else:
        form = UploadForm()

    return render(request, 'pages/upload.html', {'form': form })



def upload_info(request, slug):
    image = get_object_or_404(ImageUpload, slug=slug)

    context = {
        'image': image,
    }



    return render(request, 'pages/uploadinfo.html', context)