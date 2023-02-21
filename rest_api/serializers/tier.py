from rest_framework import serializers

from rest_api.models import AccountTier, ArbitraryTier, Tier


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


class ArbitraryTierSerializer(serializers.ModelSerializer):
    """Serializer for ArbitraryTier model"""

    class Meta:
        model = ArbitraryTier
        fields = "__all__"
