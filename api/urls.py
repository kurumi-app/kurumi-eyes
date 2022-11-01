from django.urls import path, include
from .views import *

from django.contrib.auth import views as auth_views

from rest_framework.authtoken import views



urlpatterns = [
    path("upload/", UploadView.as_view(), name="uploadapi"),
    path('api-token-auth/', views.obtain_auth_token)

]
