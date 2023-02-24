from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from rest_api.models import AccountTier, Tier
from rest_api.serializers.tier import (
    AccountTierSerializer,
    TierSerializer,
)


class TierViewSet(viewsets.ModelViewSet):
    """ViewSet for Tier model"""

    permission_classes = [IsAdminUser]
    queryset = Tier.objects.select_related()
    serializer_class = TierSerializer


class AccountTierViewSet(viewsets.ModelViewSet):
    """ViewSet for AccountTier model"""

    permission_classes = [IsAdminUser]
    queryset = AccountTier.objects.select_related()
    serializer_class = AccountTierSerializer

