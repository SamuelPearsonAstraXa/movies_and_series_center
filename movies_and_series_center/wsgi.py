import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'movies_and_series_center.settings')

application = get_wsgi_application()
