from django.urls import reverse
from rest_framework import serializers

from rest_api.models import AccountTier, Image


class ImageSerializer(serializers.ModelSerializer):
    """Serializer for Image model"""

    t_200_url = serializers.SerializerMethodField()
    t_400_url = serializers.SerializerMethodField()
    temporary_link = serializers.SerializerMethodField()
    custom_thumbnail = serializers.SerializerMethodField()

    class Meta:
        model = Image
        fields = "__all__"

    def to_representation(self, instance) -> dict:
        user = self.context["request"].user
        account_tier = AccountTier.objects.get(user=user)
        data = {}
        if account_tier.tier.name == "Basic":
            data["t_200_url"] = self.get_t_200_url(instance)

        elif account_tier.tier.name == "Premium":
            data["t_200_url"] = self.get_t_200_url(instance)
            data["t_400_url"] = self.get_t_400_url(instance)
            data[
                "original_image"
            ] = f"http://127.0.0.1:8000{instance.original_image.url}"

        elif account_tier.tier.name == "Enterprise":
            data["t_200_url"] = self.get_t_200_url(instance)
            data["t_400_url"] = self.get_t_400_url(instance)
            data[
                "original_image"
            ] = f"http://127.0.0.1:8000{instance.original_image.url}"
            data["temporary_link"] = self.get_temporary_link(instance)
        else:
            data["temporary_link"] = self.get_temporary_link(instance)
            data[
                "original_image"
            ] = f"http://127.0.0.1:8000{instance.original_image.url}"
            data["custom_thumbnail"] = self.get_custom_thumbnail(instance)
        data["uploaded_by"] = instance.uploaded_by.username
        data["created_at"] = instance.created_at
        return data

    def get_t_200_url(self, obj: Image) -> str:
        return f"http://127.0.0.1:8000{obj.t200.url}"

    def get_t_400_url(self, obj: Image) -> str:
        return f"http://127.0.0.1:8000{obj.t400.url}"

    def get_custom_thumbnail(self, obj: Image) -> str:
        return f"http://127.0.0.1:8000{obj.custom_thumbnail.url}"

    def get_fields(self, *args, **kwargs) -> dict:
        fields = super().get_fields(*args, **kwargs)
        user = self.context["request"].user
        account_tier = AccountTier.objects.get(user=user)
        if account_tier.tier.name == "Basic" or account_tier.tier.name == "Premium":
            fields["link_expiration_time"].read_only = True
            fields["uploaded_by"].read_only = True
            fields["created_at"].read_only = True
        elif account_tier.tier.name == "Enterprise":
            fields["uploaded_by"].read_only = True
            fields["created_at"].read_only = True
        else:
            fields["uploaded_by"].read_only = True
        return fields

    def get_temporary_link(self, obj: Image) -> str:
        link_expiration_time = obj.link_expiration_time
        if link_expiration_time:
            temporary_link_url = reverse("image-temporary-link", args=[obj.id])
            return self.context["request"].build_absolute_uri(temporary_link_url)
