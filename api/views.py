from .serializers import *
from uploads.models import *
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated


# Create your views here.
class UploadView(generics.CreateAPIView):

    permission_classes = (IsAuthenticated,)

    queryset = ImageUpload.objects.all()
    serializer_class = UploadSerializer