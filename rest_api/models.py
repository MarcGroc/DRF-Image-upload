from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from django_resized import ResizedImageField
from imagekit.models import ImageSpecField
from pilkit.processors import ResizeToFill


class Image(models.Model):
    original_image = models.FileField(
        upload_to=settings.MEDIA_ROOT,
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'png'])],
        default='default.jpg'
    )

    t200 = ImageSpecField(
        source='original_image',
        processors=[ResizeToFill(200, 200)],
        options={'quality': 100},
    )

    t400 = ImageSpecField(
        source='original_image',
        processors=[ResizeToFill(400, 400)],
        options={'quality': 100},
    )

    created_at = models.DateTimeField(auto_now_add=True)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.original_image.name}"


class Tier(models.Model):
    name = models.CharField(max_length=50)
    thumbnail_200 = models.BooleanField(default=True)
    thumbnail_400 = models.BooleanField(default=False)
    original_image_link = models.BooleanField(default=False)
    link_expiration = models.BooleanField(default=False)
    link_expiration_time = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class AccountTier(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tier = models.ForeignKey(Tier, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f"{self.user.username} - {self.tier.name}"
