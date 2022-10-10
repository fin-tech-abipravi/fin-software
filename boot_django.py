import os
import django
from django.conf import settings

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "api"))
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "accounts"))
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "places"))

def boot_django():
    settings.configure(
        BASE_DIR=BASE_DIR,
        DEBUG=True,
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.postgresql_psycopg2',

                'NAME': "fin1",

                'USER': "postgres",

                'PASSWORD': "123",

                'HOST': 'localhost',

                'PORT': '5432',
            }
        },
        INSTALLED_APPS=(
            'api',
            'accounts',
            'places'
        ),
        TIME_ZONE="UTC",
        USE_TZ=True,
    )
    django.setup()