from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, FileResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.db.models import Sum
from .forms import *
import datetime
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