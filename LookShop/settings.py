from pathlib import Path
<<<<<<< HEAD
=======
import os
import environ

env = environ.Env()
environ.Env.read_env()

ENVIRONMENT = env
>>>>>>> 1cb3347 (Parcheo1S)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

<<<<<<< HEAD

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '-95t%=#4o3@l-(-%ok9*h%n3!0(sdchjn%+_$5#umaj-!3bg*7'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*','https://lookshop.onrender.com']


=======
SECRET_KEY = os.environ.get('SECRET_KEY')
DEBUG = 'RENDER' not in os.environ

ALLOWED_HOSTS = ['*','https://lookshop.onrender.com']

>>>>>>> 1cb3347 (Parcheo1S)
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
<<<<<<< HEAD
    'store'
]

=======
    'LookShop',
    'store',
]


>>>>>>> 1cb3347 (Parcheo1S)
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 1cb3347 (Parcheo1S)
SESSION_COOKIE_SECURE = True
CSRR_Cookie_secure = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_SECONDS = 31536000
SECURE_REDIRECT_EXEMPT = []
SECURE_SSL_REDIRECT = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
<<<<<<< HEAD
=======
=======

>>>>>>> 15316db (version1Parcheo)
>>>>>>> 1cb3347 (Parcheo1S)
ROOT_URLCONF = 'LookShop.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'LookShop.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': BASE_DIR / 'db.sqlite3',
#    }
#}


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'bd_look',
        'USER': 'bd_look_user',
        'PASSWORD': 'qwW0IcGXsVh5vul8ZMNI0pm3sjUOeQB0',
        'HOST': 'dpg-cen40ehgp3jlcsihpf5g-a.oregon-postgres.render.com',
        'PORT': '5432',
   }
}

<<<<<<< HEAD
#
# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators
=======
<<<<<<< HEAD
=======
"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'bdpost',
        'USER': 'admin',
        'PASSWORD': 'gXndp6wYWogbMBAfj1Hk2DPhMbs5VsaB',
        'HOST': 'dpg-ceigvtkgqg4dlfbh1ip0-a.oregon-postgres.render.com',
        'PORT': '5432',
    }
}
"""
"""
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.ScryptPasswordHasher',
]
"""
>>>>>>> 15316db (version1Parcheo)
#
# Password validation
>>>>>>> 1cb3347 (Parcheo1S)

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

#LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'es-ue'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
<<<<<<< HEAD
MEDIA_URL = "/image/download/"
MEDIA_ROOT = BASE_DIR
=======
MEDIA_ROOT = os.path.join(BASE_DIR, '/image/download/')
MEDIA_URL = "/image/download/"
if not DEBUG:
    STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'


>>>>>>> 1cb3347 (Parcheo1S)
