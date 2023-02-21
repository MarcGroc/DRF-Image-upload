import os

from django.conf import settings
from django.core.management.base import BaseCommand

from rest_api.models import Image


class Command(BaseCommand):
    help = "Deletes all image objects for which the corresponding file does not exist in the media directory"

    def handle(self, *args, **options):
        media_root = settings.MEDIA_ROOT
        images = Image.objects.all()
        for image in images:
            file_path = os.path.join(media_root, str(image.original_image))
            if not os.path.isfile(file_path):
                image.delete()
                self.stdout.write(
                    self.style.SUCCESS(f"Deleted image with id {image.id}")
                )
