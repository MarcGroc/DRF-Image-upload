from rest_framework import viewsets

from rest_api.models import Image
from rest_api.serializers.image import ImageSerializer


class ImageViewSet(viewsets.ModelViewSet):
    """ViewSet for Image model"""

    queryset = Image.objects.select_related()
    serializer_class = ImageSerializer
