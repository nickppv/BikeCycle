"""
Django settings for bicycle project.

Generated by 'django-admin startproject' using Django 4.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os
from conf import MY_KEY

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = MY_KEY

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# при добавлении строк сервера, можно проверить работоспособность переопределенных функций для ошибок 404, 403, 500
# при развертывании проекта устанавливается домен сайта
ALLOWED_HOSTS = [
    'gvvd.ru'
    'localhost',
    '127.0.0.1',
    '[::1]',
    'testserver',
]


# Application definition

INSTALLED_APPS = [
    'bikes.apps.BikesConfig',
    'core.apps.CoreConfig',
    'feedback.apps.FeedbackConfig',
    'users.apps.UsersConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    # добавил капчу для формы регистрации и авторизации
    'captcha',
    'debug_toolbar',
    'django_filters',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

# для django_debug_toolbar, он запускается на этом адресе
INTERNAL_IPS = [
    "127.0.0.1",
]

# ADMINS - список людей, которые получают уведомления об ошибках кода.
# когда DEBUG=False и AdminEmailHandler настроен в LOGGING (сделано по
# умолчанию), Django отправляет этим людям по электронной почте сведения
# об исключениях, возникших в цикле запрос/ответ.
ADMINS = [('Nikolay', 'pvnick@yandex.ru'), ]

# настройки для отправки писем, включая восстановление пароля
EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_PORT = 465
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True
EMAIL_HOST_USER = 'pvnick@yandex.ru'
EMAIL_HOST_PASSWORD = 'adfpuspqqhvufsvz'
DEFAULT_FROM_EMAIL = 'pvnick@yandex.ru'

ROOT_URLCONF = 'bicycle.urls'

TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'core.context_processors.year.year',
            ],
        },
    },
]

WSGI_APPLICATION = 'bicycle.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'Etc/GMT-7'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# константа BASE_DIR определяет рабочую папку проекта и к этой папке будет
# добавлять подкаталог 'media', где будут располагаться файлы проекта
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# добавляет к url графическим медиа префик media
MEDIA_URL = '/media/'


LOGIN_URL = 'users:login'
LOGIN_REDIRECT_URL = 'bikes:index'
LOGOUT_REDIRECT_URL = 'bikes:index'

#  подключаем движок filebased.EmailBackend
if DEBUG:
    # в режиме отладки используем локальную папку для писем восстановления
    EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
    # в боевом режиме используем smtp-сервер
else:
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# указываем директорию, в которую будут складываться файлы писем
EMAIL_FILE_PATH = os.path.join(BASE_DIR, 'sent_emails')

# некоторые настройки для капчи
# остальные астройки здесь - https://django-simple-captcha.readthedocs.io/en/latest/advanced.html#configuration-toggles
CAPTCHA_FONT_SIZE = 26
CAPTCHA_LETTER_ROTATION = (-45, 45)
CAPTCHA_BACKGROUND_COLOR = '#ffffff'
CAPTCHA_TIMEOUT = 2
CAPTCHA_LENGTH = 6
# чтобы сделать больше шума - повторил аргументы в кортеже
CAPTCHA_NOISE_FUNCTIONS = ('captcha.helpers.noise_arcs',
                           'captcha.helpers.noise_dots',
                           'captcha.helpers.noise_arcs',
                           'captcha.helpers.noise_dots',
                           )


