from pathlib import Path
import dj_database_url
import os

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-n3ej-529nd_ofygu044*)w236=i8t((=to#8^imtu^f@z#p3lt'

DEBUG = False

ALLOWED_HOSTS = ["*"]

# التطبيقات
INSTALLED_APPS = [
    "jazzmin",   # لازم يكون أولاً عشان يعدل مظهر الأدمين
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main',
    'django.contrib.sitemaps',
]

# الوسطاء
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',   # ✅ مهم لتقديم static في Render
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'palmsite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],
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

WSGI_APPLICATION = 'palmsite.wsgi.application'

# قاعدة البيانات (PostgreSQL Render)
DATABASES = {
    'default': dj_database_url.config(
        default="postgresql://palmsite_db_user:4kntGkmzsL6ikHUGJEC9AltygQPdhcVK@dpg-d39rrire5dus73bnjisg-a.oregon-postgres.render.com/palmsite_db",
        conn_max_age=600,
        ssl_require=True
    )
}

# التحقق من كلمة المرور
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# اللغة والمنطقة
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Riyadh'
USE_I18N = True
USE_TZ = True

# الملفات الثابتة
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"

# ✅ إعداد WhiteNoise للتصغير والتخزين
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# الملفات الإعلامية
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / "media"

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Jazzmin settings
JAZZMIN_SETTINGS = {
    "site_title": "لوحة الإدارة",
    "site_header": "مؤسسة النخيل والشبوك",
    "site_brand": "لوحة التحكم",
    "welcome_sign": "مرحباً بك في لوحة إدارة الموقع",
    "copyright": "© 2025 مؤسسة النخيل",
    "topmenu_links": [
        {"name": "الرئيسية", "url": "admin:index", "permissions": ["auth.view_user"]},
        {"name": "الموقع", "url": "/", "new_window": True},
    ],
    "usermenu_links": [
        {"name": "تواصل معنا", "url": "/contact", "new_window": True},
    ],
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
        "main.Service": "fas fa-tools",
        "main.Product": "fas fa-leaf",
        "main.BlogPost": "fas fa-blog",
    },
    "show_ui_builder": True,
}
