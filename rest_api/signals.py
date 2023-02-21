from django.db.models.signals import post_save
from django.dispatch import receiver

from rest_api.models import Image

from .tasks import resize_image_task


@receiver(post_save, sender=Image)
def resize_image(sender, instance, **kwargs):
    resize_image_task.delay(instance.id)
