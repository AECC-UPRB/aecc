from configurations import Configuration, values

import os


class Common(Configuration):
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))

    ENVIRONMENT = values.Value(environ_prefix=None, default='development')

    SECRET_KEY = values.SecretValue(environ_prefix=None)

    DEBUG = False

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
        'apps.contact',
        'apps.users',
        'apps.blog',

        # Third party
        'allauth',
        'allauth.account',
        'allauth.socialaccount',
        'django_extensions',
        'debug_toolbar',
        'import_export',
        'taggit',
        'tinymce',
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
    # https://docs.djangoproject.com/en/dev/ref/settings/#databases
    DATABASES = values.DatabaseURLValue(
        'sqlite:///{}'.format(os.path.join(BASE_DIR, 'storage.sqlite3')))

    # Internationalization
    # https://docs.djangoproject.com/en/1.6/topics/i18n/
    LANGUAGE_CODE = 'en-us'

    TIME_ZONE = 'UTC'

    USE_I18N = True

    USE_L10N = True

    USE_TZ = True

    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/1.6/howto/static-files/

    STATIC_ROOT = '/static/'
    STATIC_URL = '/static/'

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
        os.path.join(BASE_DIR, 'static'),
    )

    TEMPLATE_DIRS = (
        os.path.join(BASE_DIR, 'templates'),
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

    TINYMCE_JS_ROOT = os.path.join(STATIC_URL, "js/tiny_mce")
    TINYMCE_JS_URL = os.path.join(STATIC_URL, "js/tiny_mce/tiny_mce_src.js")
    TINYMCE_DEFAULT_CONFIG = {
        'plugins': "table,spellchecker,paste,searchreplace",
        'theme': "advanced",
        'cleanup_on_startup': True,
        'custom_undo_redo_levels': 10,
    }
    TINYMCE_SPELLCHECKER = True
    TINYMCE_COMPRESSOR = True


class Development(Common):
    DEBUG = True

    TEMPLATE_DEBUG = DEBUG

    PROTOCOL = 'http'

    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

    # Dummy cache for development
    CACHES = {
        'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
        }
    }


class Production(Common):
    PROTOCOL = 'https'
