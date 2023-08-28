

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = 'django-insecure-$ks=2uz)nqy_k!oex8_d-4v@rh(6_tkxibga$svmy()3ilksbp'

DEBUG = True

ALLOWED_HOSTS = ['lisapremium.com', '88.198.22.18', 'www.lisapremium.com', '*']



INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'APP',
    'mpesa',
    'rest_framework',
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

ROOT_URLCONF = 'project2.urls'

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

WSGI_APPLICATION = 'project2.wsgi.application'




DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'lucy',   
        'USER': 'lucy',        
        'PASSWORD': 'lucy2023',    
        'HOST': 'localhost',            
        'PORT': '',                     
    }
}




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




LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True



STATIC_URL = 'static/'


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MPESA_CONFIG = {
        'CONSUMER_KEY': 'T3IfaH3DqCAKsu7OX9LJVCaeRtMBe8py',
        'CONSUMER_SECRET': 'nWHC3IfKx9em4bEq',
        'HOST_NAME': 'https://2987-41-89-10-241.ngrok-free.app',
        'PASS_KEY': 'bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919',
        'SAFARICOM_API': 'https://sandbox.safaricom.co.ke',
        'AUTH_URL': '/oauth/v1/generate?grant_type=client_credentials',
        'TRANSACTION_TYPE': 'CustomerBuyGoodsOnline',
        'TILL_NUMBER': '9886465',

        'SHORT_CODE': '174379'

    }