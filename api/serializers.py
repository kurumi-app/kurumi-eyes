from uploads.models import ImageUpload
from rest_framework import serializers
from django.urls import reverse

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

    # return slug after request
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['slug'] = instance.slug
        # request
        request = self.context.get('request', None)
        if request is not None:
            representation['upload_url'] = request.build_absolute_uri(reverse('upload_info', kwargs={'slug': instance.slug}))
        return representation
























































































        