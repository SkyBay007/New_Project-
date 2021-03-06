import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '-0=4ew!(%o$(+7=8tv)6woj=^!hbj%f4ob=n2e7@hba*@y)wie'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'accounts',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main',
    'catalogo',
    'social.apps.django_app.default',
    'taggit',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'peliculas.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'peliculas.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = 'staticfiles'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)

MEDIA_ROOT = os.path.join(BASE_DIR,'media')
MEDIA_URL = '/media/'

from django.core.urlresolvers import reverse_lazy

LOGIN_REDIRECT_URL = reverse_lazy('catalogo:list-movies')
# LOGIN_URL = reverse_lazy('accounts:login')
# LOGOUT_URL = reverse_lazy('accounts:logout')
# 

AUTHENTICATION_BACKENDS = (
        'django.contrib.auth.backends.ModelBackend',
        'accounts.authentication.EmailAuthBackend',
        'accounts.authentication.TelAuthBackend',
        'social.backends.facebook.Facebook2OAuth2',
        'social.backends.twitter.TwitterOAuth',
    )

SOCIAL_AUTH_FACEBOOK_KEY = '1869498409960970'
SOCIAL_AUTH_FACEBOOK_SECRET = '7620d5a3ba4f8dd02b6a3b79392f4fd3'

SOCIAL_AUTH_TWITTER_KEY = 'Bb2Q6KsShPIp4YSjlm6UEZmEm'
SOCIAL_AUTH_TWITTER_SECRET = 'UZDBgKfXbX6GaAu25IhRkgKm3bp2sKkaGLVFIHBHdQPtlUoWAw'

SOCIAL_AUTH_FACEBOOK_SCOPE= ['email']

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'hugo.enscruz@gmail.com'
EMAIL_HOST_PASSWORD = 'alucard::9412'
EMAIL_PORT = 587
EMAIL_USE_TLS = True