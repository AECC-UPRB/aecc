"""
Django settings for aecc project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'jl1gh(r9))nyva)lv@-lty66^k6bn=^y4(iteic#2cv+ud-xnl'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    # Apps
    'apps.events',
    'apps.people',
    'apps.contact',
    'apps.users',
    'apps.members',
    'apps.blogs',

    # Third party
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'django_extensions'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'aecc.urls'

WSGI_APPLICATION = 'aecc.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'storage.db'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]

#MEDIA_ROOT = os.path.join(BASE_DIR, 'static')

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.core.context_processors.request",
    "django.contrib.auth.context_processors.auth",
    "allauth.account.context_processors.account",
    "allauth.socialaccount.context_processors.socialaccount",
)

AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
)

SITE_ID = 1

STATICFILES_DIRS = (
    ('assets', os.path.join(BASE_DIR, 'static')),
)

AUTH_USER_MODEL = "users.User"

# auth and allauth settings
LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/accounts/login/'
ACCOUNT_EMAIL_VERIFICATION = "none"
ACCOUNT_EMAIL_SUBJECT_PREFIX = '[AECC]'
ACCOUNT_LOGOUT_ON_GET = True
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_CONFIRM_EMAIL_ON_GET = True
ACCOUNT_LOGOUT_REDIRECT_URL = LOGIN_URL
ACCOUNT_USERNAME_BLACKLIST = ['admin']
ACCOUNT_USER_MODEL_USERNAME_FIELD = "email"
ACCOUNT_SIGNUP_FORM_CLASS = 'apps.users.forms.SignupForm'
ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_USERNAME_REQUIRED = False

EMAIL_USE_TLS = True

EMAIL_HOST = "smtp.googlemail.com"

EMAIL_PORT = 587

EMAIL_HOST_USER = "example@example.com"

EMAIL_HOST_PASSWORD = "example"

RECAPTCHA_PUBLIC_KEY = '76wtgdfsjhsydt7r5FFGFhgsdfytd656sad75fgh'

RECAPTCHA_PRIVATE_KEY = '98dfg6df7g56df6gdfgdfg65JHJH656565GFGFGs'

RECAPTCHA_USE_SSL = True
