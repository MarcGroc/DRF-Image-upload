from rest_framework import serializers

from rest_api.models import AccountTier, Tier


class TierSerializer(serializers.ModelSerializer):
    """Tier default serializer"""

    class Meta:
        model = Tier
        fields = "__all__"


class AccountTierSerializer(serializers.ModelSerializer):
    """Serializer for AccountTier model"""

    class Meta:
        model = AccountTier
        fields = "__all__"

