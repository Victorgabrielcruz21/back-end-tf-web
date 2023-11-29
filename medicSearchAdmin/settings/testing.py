from .settings import *

DEBUG = True

# Crie a secret key para seu ambiente de desenvolvimento
SECRET_KEY = 'ixb62ha#ts=ab4t2u%p1_62-!5w2j==j6dj$!z(@*m+-h'


ALLOWED_HOSTS = ['*']

DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': 'Bandejao',
    'USER': 'Victorgabrielcruz',
    'PASSWORD': 'zRWsGCr8J2Ey',
    'HOST': 'ep-spring-rice-69313704.us-east-2.aws.neon.tech',
    'PORT': '5432',
    'OPTIONS': {'sslmode': 'require'},
  }
}