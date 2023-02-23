from django.shortcuts import redirect
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated

from rest_api.models import Image
from rest_api.serializers.image import ImageSerializer
from rest_api.tasks import image_upload


class ImageList(viewsets.ModelViewSet):
    """Viewset for Image model"""

    serializer_class = ImageSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Image.objects.filter(uploaded_by=self.request.user)

    def perform_create(self, serializer):
        serializer.save(uploaded_by=self.request.user)
        image_upload.delay(self.request.user.id)

    @action(detail=True, methods=["get"])
    def temporary_link(self, request, pk=None):
        obj = self.get_object()
        return redirect(obj.original_image.url)
