from django.contrib.auth.models import User
from django.core.validators import (
    FileExtensionValidator,
    MaxValueValidator,
    MinValueValidator,
)
from django.db import models
from imagekit.models import ImageSpecField
from pilkit.processors import ResizeToFill


class Tier(models.Model):
    name = models.CharField(max_length=50, unique=True)
    thumbnail_200 = models.BooleanField(default=True)
    thumbnail_400 = models.BooleanField(default=False)
    custom_thumbnail = models.BooleanField(default=False)
    custom_thumbnail_size = models.IntegerField(
        null=True,
        blank=True,
        validators=[MinValueValidator(1), MaxValueValidator(1000)],
    )
    original_image_link = models.BooleanField(default=False)
    link_expiration = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class AccountTier(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tier = models.ForeignKey(Tier, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f"{self.tier.name}"


class Image(models.Model):
    original_image = models.FileField(
        upload_to="media/",
        validators=[FileExtensionValidator(allowed_extensions=["jpg", "png"])],
        default="default.jpg",
    )

    t200 = ImageSpecField(
        source="original_image",
        processors=[ResizeToFill(200, 200)],
        options={"quality": 100},
    )

    t400 = ImageSpecField(
        source="original_image",
        processors=[ResizeToFill(400, 400)],
        options={"quality": 100},
    )
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    custom_thumbnail = ImageSpecField(
        source="original_image",
        processors=[ResizeToFill(100, 100)],
        options={"quality": 100},
    )

    created_at = models.DateTimeField(auto_now_add=True)
    link_expiration_time = models.IntegerField(
        null=True,
        blank=True,
        validators=[MinValueValidator(300), MaxValueValidator(3000)],
    )

    def __str__(self):
        return f"{self.original_image}"

    def save(self, *args, **kwargs):
        self.tier = AccountTier.objects.get(user=self.uploaded_by)
        if self.tier.tier.custom_thumbnail:
            custom_thumbnail_size = self.tier.tier.custom_thumbnail_size
            print(
                f"custom_thumbnail_size: {custom_thumbnail_size}--------------------------"
            )
            self.custom_thumbnail = ImageSpecField(
                source="original_image",
                processors=[
                    ResizeToFill(f"{custom_thumbnail_size}", f"{custom_thumbnail_size}")
                ],
                options={"quality": 100},
            )
        super().save(*args, **kwargs)
