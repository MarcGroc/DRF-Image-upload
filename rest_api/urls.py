from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework.routers import DefaultRouter
# from rest_api.views.tier import TierViewSet
from rest_api.views.image import ImageViewSet

router = DefaultRouter()
# router.register(r"tier", TierViewSet, basename="tier")
router.register(r"image", ImageViewSet, basename="image")

urlpatterns = [
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path("docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="docs"),
    path("api/", include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
