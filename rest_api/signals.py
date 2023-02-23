from django.db.models.signals import post_save
from django.dispatch import receiver
from imagekit.models import ImageSpecField
from pilkit.processors import ResizeToFill

from rest_api.models import Tier


@receiver(post_save, sender=Tier)
def update_custom_thumbnails(sender, instance, **kwargs):
    if instance.custom_thumbnail_size is not None:
        for image in instance.image_set.all():
            if instance.custom_thumbnail:
                custom_thumbnail_size = instance.custom_thumbnail_size
                image.custom_thumbnail = ImageSpecField(
                    source="original_image",
                    processors=[
                        ResizeToFill(custom_thumbnail_size, custom_thumbnail_size)
                    ],
                    options={"quality": 100},
                )
                image.save()
