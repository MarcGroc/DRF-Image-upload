from celery import shared_task
from imagekit.processors import ResizeToFill

from rest_api.models import Image


@shared_task
def resize_image_task(image_id):
    image = Image.objects.get(id=image_id)
    t200_processor = ResizeToFill(200, 200)
    t400_processor = ResizeToFill(400, 400)
    image.t200 = t200_processor.process(image.original_image)
    image.t400 = t400_processor.process(image.original_image)
    image.save()
