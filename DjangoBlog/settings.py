"""
Django settings for DjangoBlog project.

Generated by 'django-admin startproject' using Django 1.10.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '&3g0bdza#c%dm1lf%5gi&0-*53p3t0m*hmcvo29cn^$ji7je(c'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# ALLOWED_HOSTS = []
ALLOWED_HOSTS = ['www.lylinux.net', '127.0.0.1']
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'pagedown',
    'haystack',
    'blog',
    'accounts',
    'comments',
    'oauth'
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.gzip.GZipMiddleware',
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.http.ConditionalGetMiddleware',
]

ROOT_URLCONF = 'DjangoBlog.urls'

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
                'blog.context_processors.seo_processor'
            ],
        },
    },
]

WSGI_APPLICATION = 'DjangoBlog.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'djangoblog',
        'USER': os.environ.get('DJANGO_MYSQL_USER'),
        'PASSWORD': os.environ.get('DJANGO_MYSQL_PASSWORD'),
        'HOST': os.environ.get('DJANGO_MYSQL_HOST'),
        'PORT': 3306,
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

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/


SITE_ROOT = os.path.dirname(os.path.abspath(__file__))
SITE_ROOT = os.path.abspath(os.path.join(SITE_ROOT, '../'))

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'DjangoBlog.whoosh_cn_backend.WhooshEngine',
        'PATH': os.path.join(os.path.dirname(__file__), 'whoosh_index'),
    },
}
# 自动更新搜索索引
HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'

STATIC_ROOT = os.path.join(SITE_ROOT, 'collectedstatic')

STATIC_URL = '/static/'
STATICFILES = os.path.join(BASE_DIR, 'static')

AUTH_USER_MODEL = 'accounts.BlogUser'
LOGIN_URL = '/login/'

TIME_FORMAT = '%Y-%m-%d %H:%M:%S'
DATE_TIME_FORMAT = '%Y-%m-%d'

SITE_NAME = 'Django Blog'
SITE_URL = 'http://blog.lylinux.org'
SITE_DESCRIPTION = '大巧无工,重剑无锋.'
SITE_SEO_DESCRIPTION = '小站主要用来分享和记录学习经验,教程,记录个人生活的点滴以及一些随笔.欢迎大家访问小站'
SITE_SEO_KEYWORDS = 'linux,apache,mysql,服务器,ubuntu,shell,web,csharp,.net,asp,mac,swift'
ARTICLE_SUB_LENGTH = 300
SHOW_GOOGLE_ADSENSE = True
# bootstrap颜色样式
BOOTSTRAP_COLOR_TYPES = [
    'default', 'primary', 'success', 'info', 'warning', 'danger'
]

# 侧边栏文章数目
SIDEBAR_ARTICLE_COUNT = 10
# 侧边栏评论数目
SIDEBAR_COMMENT_COUNT = 5

# 分页
PAGINATE_BY = 10
# http缓存时间
CACHE_CONTROL_MAX_AGE = 2592000
# cache setting

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '192.168.21.130:11211',
    },
    'localmem': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake',
    }
}
CACHE_MIDDLEWARE_SECONDS = 360000
CACHE_MIDDLEWARE_KEY_PREFIX = "djangoblog"
CACHE_MIDDLEWARE_ALIAS = 'default'
OAHUTH = {
    'sina': {
        'appkey': '3161614143',
        'appsecret': 'ee17c099317f872eeddb25204ea46721',
        'callbackurl': 'http://blog.lylinux.org/oauth/weibo'
    }
}

SITE_ID = 2