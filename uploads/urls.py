from django.urls import path, include
from .views import *

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("kurumiadminsysuploads/", admin_uploads, name="admin_uploads"),
    path("delupload/<int:pk>/", adm_delete_upload, name="del_upload"),
    path("deluser/<int:pk>/", adm_ban_user, name="del_user"),

    path("", home, name="home"),
    path("dashboard/", dashboard, name="dashboard"),
    path("upload/", upload, name="upload"),
    path("upload/<slug:slug>/", upload_info, name="upload_info"),
    path("download/<slug:slug>/", download_image, name="download"),
    path("myuploads/", my_uploads, name="my_uploads"),

    path("settings/", user_settings, name="settings"),
    path("sharex/", sharex_conf, name="sharex_conf"),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
