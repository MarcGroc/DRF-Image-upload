from rest_framework import serializers

from rest_api.models import Tier


class TierSerializer(serializers.ModelSerializer):
    """Tier default serializer"""

    class Meta:
        model = Tier
        fields = "__all__"
