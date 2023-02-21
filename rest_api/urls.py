from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from rest_api.views.image import ImageList
from rest_api.views.tier import AccountTierViewSet, ArbitraryTierViewSet, TierViewSet

router = DefaultRouter()
router.register(r"tier", TierViewSet, basename="tier")
router.register(r"image", ImageList, basename="image")
router.register(r"account-tier", AccountTierViewSet, basename="account-tier")
router.register(r"arbitrary-tier", ArbitraryTierViewSet, basename="arbitrary-tier")


urlpatterns = [
    path("api/", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
