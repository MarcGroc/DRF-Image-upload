from django.db.models.signals import pre_save
from django.dispatch import receiver

from rest_api.models import Image


@receiver(pre_save, sender=Image)
def create_thumbnails(sender, instance, **kwargs):
    instance.t200.generate()
    instance.t400.generate()
