from uploads.models import ImageUpload
from rest_framework import serializers

class UploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageUpload
        read_only_fields = ['user', 'slug', 'uploaded_at', 'image_size']
        fields = (
            'image',
        )

    def create(self, validated_data):
        user = self.context['request'].user
        return ImageUpload.objects.create(user=user, **validated_data)























































































        