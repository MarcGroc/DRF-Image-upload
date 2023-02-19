from rest_framework import serializers

from rest_api.models import Image


class ImageSerializer(serializers.ModelSerializer):
    thumbnail_200_url = serializers.SerializerMethodField()
    thumbnail_400_url = serializers.SerializerMethodField()

    class Meta:
        model = Image
        fields = "__all__"

    def get_thumbnail_200_url(self, obj):
        return f"http://127.0.0.1:8000{obj.t200.url}"

    def get_thumbnail_400_url(self, obj):
        return f"http://127.0.0.1:8000{obj.t400.url}"
