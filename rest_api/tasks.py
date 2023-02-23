from datetime import datetime, timedelta, timezone

from celery import shared_task
from django.contrib.auth.models import User

from rest_api.models import Image


@shared_task
def check_link_expiration():
    images = Image.objects.exclude(link_expiration_time__isnull=True)
    for image in images:
        if image.link_expiration_time:
            expiration_time = timedelta(seconds=image.link_expiration_time)
            if datetime.now(timezone.utc) > image.created_at + expiration_time:
                image.link_expiration_time = None
                image.save()
    return "Expired links deleted successfully"


@shared_task
def image_upload(user_id):
    user = User.objects.get(id=user_id)
    images = Image.objects.filter(uploaded_by=user)
    for image in images:
        image.save()
    return "Image uploaded successfully"


@shared_task
def delete_not_existing_images():
    images = Image.objects.all()
    for image in images:
        if not image.original_image:
            image.delete()
    return "Not existing images deleted successfully"
