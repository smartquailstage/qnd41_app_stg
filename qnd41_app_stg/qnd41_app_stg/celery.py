import os
from celery import Celery

# Establecer la configuración por defecto de Django para el programa 'celery'.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'qnd41_app_stg.settings')

# Crear una instancia de la aplicación Celery
app = Celery('qnd41_app_stg')

# Cargar la configuración de Celery desde el módulo de configuración de Django
app.config_from_object('django.conf:settings', namespace='CELERY')

# Autodescubrir tareas definidas en la aplicación Django
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
