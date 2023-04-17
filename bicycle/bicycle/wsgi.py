"""
WSGI config for bicycle project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

# application = get_wsgi_application()

# -*- coding: utf-8 -*-

sys.path.insert(0, '/home/k/kolazig/gvvd.ru/bicycle')
sys.path.insert(1, '/home/k/kolazig/gvvd.ru/venv_django/lib/python3.9/site-packages/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'bicycle.settings'
application = get_wsgi_application()
