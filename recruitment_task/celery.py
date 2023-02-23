import os
from datetime import timedelta

from celery import Celery
from celery.schedules import crontab
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "recruitment_task.settings")
app = Celery("recruitment_task")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

app.conf.beat_schedule = {
    'check_link_expiration': {
        'task': 'rest_api.tasks.check_link_expiration',
        'schedule': timedelta(seconds=60),
    },
    'delete_not_existing_images': {
        'task': 'rest_api.tasks.delete_not_existing_images',
        'schedule': timedelta(minutes=5),
    },
}
