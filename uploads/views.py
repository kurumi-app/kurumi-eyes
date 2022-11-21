from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, FileResponse
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required

from django.contrib.auth import get_user_model
from django.db.models import Sum
from rest_framework.authtoken.models import Token
from .forms import *
import datetime
import json 

# Create your views here.

login_url = 'login'

def home(request):
    return render(request, 'pages/home.html')

@login_required(login_url=login_url)
def dashboard(request):
    context = {
        'users': get_user_model().objects.count(),
        'uploads': ImageUpload.objects.count(),
        'uploads_today': ImageUpload.objects.filter(uploaded_at__date=datetime.date.today()).count(),
        'average_daily_uploads': ImageUpload.objects.filter(uploaded_at__date=datetime.date.today()).count() / datetime.date.today().day,
        'storage_used': ImageUpload.objects.all().aggregate(Sum('image_size'))['image_size__sum'],
        'last_created_user_time': get_user_model().objects.latest('date_joined').date_joined,
        'last_upload_time': ImageUpload.objects.last().uploaded_at,
        'last_image_size': ImageUpload.objects.last().image_size,
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


def download_image(request, slug):
    path_to_file = get_object_or_404(ImageUpload, slug=slug).image.path
    response = FileResponse(open(path_to_file, 'rb'))
    file_name = path_to_file.split('/')[-1]
    response['Content-Disposition'] = f'attachment; filename={file_name}'
    return response


def my_uploads(request):
    uploads = ImageUpload.objects.filter(user=request.user)
    context = {
        'uploads': uploads,
    }
    return render(request, 'pages/myuploads.html', context)

# settings

def user_settings(request):
    return render(request, 'pages/settings.html')

def sharex_conf(request):
    user = request.user
    token = Token.objects.get(user=user)

    data = {
    "Version": "1.0.0",
    "Name": "kurumi-eyes",
    "DestinationType": "ImageUploader, FileUploader",
    "RequestMethod": "POST",
    "RequestURL": "https://kurumi-eyes.cyou/api/upload/",
    "Headers": {
        "Authorization": f"Token {token}"
    },
    "Body": "MultipartFormData",
    "FileFormName": "image",
    "URL": "{json:upload_url}",
    "ErrorMessage": "{json:displayMessage}"
    }

    with open(f'{user}.sxcu', 'w') as f:
        json.dump(data, f, indent=2)

    response = FileResponse(open(f'{user}.sxcu', 'rb'))
    response['Content-Disposition'] = f'attachment; filename={user}.sxcu'
    return response


    
# Admin Misc

def admin_uploads(request):
    uploads = ImageUpload.objects.all()

    context = {
        'uploads': uploads,
    }
    return render(request, 'pages/alluploads.html', context)

@staff_member_required
def adm_delete_upload(request, pk):
    upload = ImageUpload.objects.get(pk=pk)
    upload.delete()
    return redirect('admin_uploads')

@staff_member_required
def adm_ban_user(request, pk):
    user = get_user_model().objects.get(pk=pk)
    user.delete()
    return redirect('admin_uploads')
