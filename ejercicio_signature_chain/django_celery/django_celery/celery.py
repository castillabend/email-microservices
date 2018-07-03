from __future__ import absolute_import
import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_celery.settings')
app = Celery('django_celery')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
        'periodic task': {
        'task':'django_celery.shipper.tasks.create_excel',
        # Cada minuto
        'schedule': crontab(minute=1),
    },
}

app.conf.beat_schedule = {
        'periodic task2': {
        'task':'django_celery.shipper.tasks.send_mail',
        # Cada minuto
        'schedule': crontab(minute=1),
    },
}

app.conf.beat_schedule = {
        'periodic task3': {
        'task':'django_celery.shipper.tasks.clean_directory',
        # Cada minuto
        'schedule': crontab(minute=1),
    },
}


@app.task(bind=True)
def test_task(self):
    print(self.request)
