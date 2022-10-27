from django.urls import path, include
from .views import *

from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", home, name="home"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
