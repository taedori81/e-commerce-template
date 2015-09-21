from .base import *


DEBUG = env('DEBUG')
TEMPLATE_DEBUG = False
SECRET_KEY = env('SECRET_KEY')

EMAIL_BACKEND = ('django.core.mail.backends.%s.EmailBackend' %
                 env('EMAIL_BACKEND_MODULE'))
EMAIL_HOST = env('EMAIL_HOST')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_PORT = env('EMAIL_PORT')
EMAIL_USE_TLS = env('EMAIL_USE_TLS')
DEFAULT_FROM_EMAIL = env('DEFAULT_FROM_EMAIL')

ALLOWED_HOSTS = env('ALLOWED_HOSTS').split()

try:
    from .local import *
except ImportError:
    pass
