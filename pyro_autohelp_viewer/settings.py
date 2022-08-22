import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

DEBUG = os.environ.get("IS_DEV", False)
SERVING_DOMAIN = os.environ.get("SERVING_DOMAIN", False)
if not SERVING_DOMAIN:
    if not DEBUG:
        raise ValueError("Expected environment variable SERVING_DOMAIN with the domain")

    SERVING_DOMAIN = "*"

CSRF_TRUSTED_ORIGINS = [f"https://{SERVING_DOMAIN}"]
ALLOWED_HOSTS = [SERVING_DOMAIN]
X_FRAME_OPTIONS = "SAMEORIGIN"
if DEBUG:
    ALLOWED_HOSTS = ["*"]

ROOT_URLCONF = "pyro_autohelp_viewer.urls"
SECRET_KEY = (
    "django-insecure-sbplyrc(9o$r#^*gftuyghddi=57f)2j1=pedjn+!!233dwad78g54&^djzx7!lt$"
)
if not DEBUG:
    SECRET_KEY = os.environ["SECRET_KEY"]


INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "base",
    "api",
]

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

ROOT_URLCONF = "pyro_autohelp_viewer.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "pyro_autohelp_viewer.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases


force_postgres = os.environ.get("FORCE_POSTGRES", False)
if DEBUG and not force_postgres:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }
else:
    if not os.environ.get("POSTGRES_NAME"):
        raise ValueError("Misconfiguration of postgres environment.")

    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": os.environ.get("POSTGRES_NAME"),
            "USER": os.environ.get("POSTGRES_USER"),
            "PASSWORD": os.environ.get("POSTGRES_PASSWORD"),
            "HOST": os.environ.get("POSTGRES_HOST"),
            "PORT": 5432,
        }
    }


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


USE_TZ = True
USE_I18N = True
TIME_ZONE = "UTC"
LANGUAGE_CODE = "en-us"
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

NINJA_DOCS_VIEW = "redoc"

if not DEBUG and not os.environ.get("API_KEY"):
    raise ValueError("API_KEY is a required enviroment variable in production.")
