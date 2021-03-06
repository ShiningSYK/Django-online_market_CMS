"""
Django settings for CMS project.

Generated by 'django-admin startproject' using Django 2.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
from django.contrib import admin

admin.AdminSite.site_title = '青竹|管理系统'
admin.AdminSite.site_header = '青竹管理系统'

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'tj38(rd#=tm*x2$*jwc%sb)oyc)lj*pm8_3w)or75uxyw6e4^h'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'simpleui',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'activity',
    'commodity',
    'order',
    'user',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_ALLOW_ALL = True
CORS_ORIGIN_WHITELIST = (
    '*'
)

CORS_ALLOW_METHODS = (
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
    'VIEW',
)

CORS_ALLOW_HEADERS = (
    'XMLHttpRequest',
    'X_FILENAME',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'users-agent',
    'x-csrftoken',
    'x-requested-with',
    'Pragma',
)
# APPEND_SLASH=False
ROOT_URLCONF = 'CMS.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'CMS.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'web_cms',
        'USER': 'root',
        'PASSWORD': 'syksyk19980825',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STARIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
MEDIA_ROOT = os.path.join(BASE_DIR, 'media').replace('\\', '/')
MEDIA_URL = '/media/'

# simpleui 设置
# 首页显示服务器、python、django、simpleui相关信息
SIMPLEUI_HOME_INFO = False
# 使用离线模式
SIMPLEUI_STATIC_OFFLINE = True

# 自定义SIMPLEUI的Logo
SIMPLEUI_LOGO = '/static/logo.png/'

# 让simpleui 不要收集相关信息
SIMPLEUI_ANALYSIS = False

SIMPLEUI_CONFIG = {
    # 该字段用于告诉simpleui，是否需要保留系统默认的菜单，
    # 默认为False，不保留，如果改为True，自定义和系统菜单将会并存
    'system_keep': False,

    # 该字段用于告诉simpleui，是否需要开启过滤显示菜单和排序功能。
    # 默认可以不用填写，缺省配置为默认排序，不对菜单进行过滤和排序。
    # 开启认为传一个列表，如果列表为空，则什么也不显示。列表中的每个元素要对应到menus里面的name字段
    # 'menu_display': ['Simpleui', '测试', '权限认证', '动态菜单测试'],

    # 该字段用于告诉simpleui，是否需要开启动态菜单功能。
    # 默认可以不用填写，缺省配置为False，不开启动态菜单功能。开启为True，开启后，每次用户登陆都会刷新左侧菜单配置。
    # 需要注意的是：开启后每次访问admin都会重读配置文件，所以会带来额外的消耗。
    'dynamic': False,
    'menus': [
        {
            'name': '系统管理',
            'icon': 'fas fa-user-shield',
            'models': [
                {
                    'name': '管理员信息',
                    'url': 'auth/user/'
                }]
        },
        {
            'app': 'user',
            'name': '用户管理',
            'icon': 'fa fa-user',
            'models': [
                {
                    'name': '用户信息',
                    'url': 'user/userinfo/'
                },
                {
                    'name': '用户订单',
                    'url': 'user/userorder'
                },
                {
                    'name': '用户购物车',
                    'url': 'user/cartdetail'
                },
                {
                    'name': '用户订单详情',
                    'url': 'order/orderdetail'
                }
            ]
        },
        {
            'name': '商品管理',
            'icon': 'fa fa-user',
            'models': [
                {
                    'name': '商品类型',
                    'url': 'commodity/commoditytype'
                },
                {
                    'name': '商品图片',
                    'url': 'commodity/commodityimage'
                },
                {
                    'name': '商品详情',
                    'url': 'commodity/commoditydetail'
                }
            ]
        },
        {
            'name': '活动管理',
            'icon': 'fa fa-user',
            'models': [
                {
                    'name': '活动类型',
                    'url': 'activity/activitytype'
                },
                {
                    'name': '活动详情',
                    'url': 'activity/activitydetail'
                },
                {
                    'name': '活动商品',
                    'url': 'activity/relactivitycommodity'
                }
            ]
        }
    ]
}
