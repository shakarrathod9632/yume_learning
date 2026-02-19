from pathlib import Path
import os
import dj_database_url

# --------------------------------------------------
# BASE DIRECTORY
# --------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# --------------------------------------------------
# SECURITY
# --------------------------------------------------
SECRET_KEY = os.environ.get("SECRET_KEY", "unsafe-secret-key-change-in-production")

DEBUG = os.environ.get("DEBUG", "True").lower() == "true"

# --------------------------------------------------
# ALLOWED HOSTS
# --------------------------------------------------
ALLOWED_HOSTS = []

if DEBUG:
    ALLOWED_HOSTS = ["127.0.0.1", "localhost"]
else:
    render_hostname = os.environ.get("RENDER_EXTERNAL_HOSTNAME")
    if render_hostname:
        ALLOWED_HOSTS.append(render_hostname)

    extra_hosts = os.environ.get("ALLOWED_HOSTS")
    if extra_hosts:
        ALLOWED_HOSTS.extend([host.strip() for host in extra_hosts.split(",")])

    if not ALLOWED_HOSTS:
        raise Exception("ALLOWED_HOSTS must be set in production!")

# --------------------------------------------------
# CSRF TRUSTED ORIGINS
# --------------------------------------------------
CSRF_TRUSTED_ORIGINS = []

if not DEBUG:
    render_hostname = os.environ.get("RENDER_EXTERNAL_HOSTNAME")
    if render_hostname:
        CSRF_TRUSTED_ORIGINS.append(f"https://{render_hostname}")

    extra_hosts = os.environ.get("ALLOWED_HOSTS")
    if extra_hosts:
        for host in extra_hosts.split(","):
            CSRF_TRUSTED_ORIGINS.append(f"https://{host.strip()}")

# --------------------------------------------------
# APPLICATIONS
# --------------------------------------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'mathfilters',

    # Local Apps
    'yume_site',
]

# --------------------------------------------------
# MIDDLEWARE
# --------------------------------------------------
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",

    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# --------------------------------------------------
# ROOT URL
# --------------------------------------------------
ROOT_URLCONF = 'yume_backend.urls'

# --------------------------------------------------
# TEMPLATES
# --------------------------------------------------
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

# --------------------------------------------------
# WSGI
# --------------------------------------------------
WSGI_APPLICATION = 'yume_backend.wsgi.application'

# --------------------------------------------------
# DATABASE
# --------------------------------------------------
if DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.environ.get("DB_NAME", "yume_learning"),
            'USER': os.environ.get("DB_USER", "postgres"),
            'PASSWORD': os.environ.get("DB_PASSWORD", ""),
            'HOST': os.environ.get("DB_HOST", "localhost"),
            'PORT': os.environ.get("DB_PORT", "5432"),
        }
    }
else:
    DATABASES = {
        'default': dj_database_url.config(
            default=os.environ.get("DATABASE_URL"),
            conn_max_age=600,
            ssl_require=True
        )
    }

# --------------------------------------------------
# PASSWORD VALIDATORS
# --------------------------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# --------------------------------------------------
# INTERNATIONALIZATION
# --------------------------------------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# --------------------------------------------------
# STATIC FILES
# --------------------------------------------------
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# --------------------------------------------------
# MEDIA FILES
# --------------------------------------------------
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# --------------------------------------------------
# DEFAULT PRIMARY KEY
# --------------------------------------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# --------------------------------------------------
# SECURITY SETTINGS (Production)
# --------------------------------------------------
if not DEBUG:
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SECURE_HSTS_SECONDS = 31536000
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True





# import dj_database_url
# from pathlib import Path
# import os




# # --------------------------------------------------
# # BASE DIRECTORY
# # --------------------------------------------------
# BASE_DIR = Path(__file__).resolve().parent.parent


# # --------------------------------------------------
# # SECURITY SETTINGS
# # --------------------------------------------------
# # SECRET_KEY = 'django-insecure-pg#j!cq4cu5a9km@m$%gs!m6h3hu4g!)p+vx&1ipsco1e04ffw'

# # DEBUG = True


# SECRET_KEY = os.environ.get("SECRET_KEY", "dev-test-secret-key")

# DEBUG = True  # Render env will override

# ALLOWED_HOSTS = [
#     "localhost",
#     "127.0.0.1",
#     ".onrender.com",
# ]


# # ALLOWED_HOSTS = []


# # --------------------------------------------------
# # APPLICATIONS
# # --------------------------------------------------
# INSTALLED_APPS = [
#     'django.contrib.admin',
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.messages',
#     'django.contrib.staticfiles',

#     'mathfilters',
#     # Local Apps
#     'yume_site',
# ]


# # --------------------------------------------------
# # MIDDLEWARE
# # --------------------------------------------------
# MIDDLEWARE = [
#     "django.middleware.security.SecurityMiddleware",
#     "whitenoise.middleware.WhiteNoiseMiddleware",
#     'django.middleware.security.SecurityMiddleware',
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'django.middleware.common.CommonMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
#     'django.middleware.clickjacking.XFrameOptionsMiddleware',
# ]


# # --------------------------------------------------
# # URL CONFIGURATION
# # --------------------------------------------------
# ROOT_URLCONF = 'yume_backend.urls'


# # --------------------------------------------------
# # TEMPLATES
# # --------------------------------------------------
# TEMPLATES = [
#     {
#         'BACKEND': 'django.template.backends.django.DjangoTemplates',
#         'DIRS': [BASE_DIR / 'templates'],
#         'APP_DIRS': True,
#         'OPTIONS': {
#             'context_processors': [
#                 'django.template.context_processors.debug',
#                 'django.template.context_processors.request',
#                 'django.contrib.auth.context_processors.auth',
#                 'django.contrib.messages.context_processors.messages',
#             ],
#         },
#     },
# ]


# # --------------------------------------------------
# # WSGI
# # --------------------------------------------------
# WSGI_APPLICATION = 'yume_backend.wsgi.application'


# # --------------------------------------------------
# # DATABASE (PostgreSQL)
# # --------------------------------------------------
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'yume_learning',
#         'USER': 'postgres',
#         'PASSWORD': 'sakku@123',
#         'HOST': 'localhost',
#         'PORT': '5432',
#     }
# }


# MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')



# MEDIA_URL = "/media/"
# MEDIA_ROOT = BASE_DIR / "media"

# # --------------------------------------------------
# # PASSWORD VALIDATION
# # --------------------------------------------------
# AUTH_PASSWORD_VALIDATORS = [
#     {
#         'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
#     },
# ]


# # --------------------------------------------------
# # INTERNATIONALIZATION
# # --------------------------------------------------
# LANGUAGE_CODE = 'en-us'

# TIME_ZONE = 'UTC'

# USE_I18N = True
# USE_TZ = True


# # --------------------------------------------------
# # STATIC FILES
# # --------------------------------------------------
# STATIC_URL = '/static/'

# STATICFILES_DIRS = [
#     BASE_DIR / 'static',
# ]

# STATIC_ROOT = BASE_DIR / 'staticfiles'


# # --------------------------------------------------
# # DEFAULT PRIMARY KEY
# # --------------------------------------------------
# DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'







