import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'async_order_system.settings')

app = Celery('async_order_system')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()