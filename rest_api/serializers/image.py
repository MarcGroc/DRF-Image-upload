from datetime import datetime, timedelta

from django.utils.text import slugify
from rest_framework import serializers

from rest_api.models import AccountTier, Image


class ImageSerializer(serializers.ModelSerializer):
    """Serializer for Image model"""

    t_200_url = serializers.SerializerMethodField()
    t_400_url = serializers.SerializerMethodField()
    temporary_link = serializers.SerializerMethodField()

    class Meta:
        model = Image
        fields = "__all__"

    def to_representation(self, instance) -> dict:
        user = self.context["request"].user
        account_tier = AccountTier.objects.get(user=user)
        data = {}
        if account_tier.tier_id == 1:
            data["t_200_url"] = self.get_t_200_url(instance)

        elif account_tier.tier_id == 2:
            data["t_200_url"] = self.get_t_200_url(instance)
            data["t_400_url"] = self.get_t_400_url(instance)
            data[
                "original_image"
            ] = f"http://127.0.0.1:8000{instance.original_image.url}"

        elif account_tier.tier_id == 3:
            data["t_200_url"] = self.get_t_200_url(instance)
            data["t_400_url"] = self.get_t_400_url(instance)
            data[
                "original_image"
            ] = f"http://127.0.0.1:8000{instance.original_image.url}"
            data["temporary_link"] = self.get_temporary_link(instance)
            if account_tier.user.id == 3:
                data["link_expiration"] = self.get_temporary_link(instance)
                data["link_expiration_time"] = instance.link_expiration_time
        data["uploaded_by"] = instance.uploaded_by.username
        data["created_at"] = instance.created_at
        return data

    def get_t_200_url(self, obj: Image) -> str:
        return f"http://127.0.0.1:8000{obj.t200.url}"

    def get_t_400_url(self, obj: Image) -> str:
        return f"http://127.0.0.1:8000{obj.t400.url}"

    def get_temporary_link(self, obj: Image) -> str:
        link_expiration_time = obj.link_expiration_time
        if link_expiration_time:
            slug = slugify(f"{obj.original_image}")
            expiration_time = datetime.now() + timedelta(seconds=link_expiration_time)
            temporary_link = (
                f"http://127.0.0.1:8000/{slug}/{expiration_time.timestamp()}"
            )
            return temporary_link

    def get_fields(self, *args, **kwargs) -> dict:
        fields = super().get_fields(*args, **kwargs)
        user = self.context["request"].user
        account_tier = AccountTier.objects.get(user=user)

        if account_tier.tier_id == 1 or account_tier.tier_id == 2:
            fields["link_expiration_time"].read_only = True
            fields["uploaded_by"].read_only = True
            fields["created_at"].read_only = True
        elif account_tier.tier_id == 3:
            fields["uploaded_by"].read_only = True
            fields["created_at"].read_only = True
        return fields
