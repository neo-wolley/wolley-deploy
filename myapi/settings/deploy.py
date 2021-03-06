from .base import *


# secret key 보호를 위한 작업
env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)

# reading .env file
environ.Env.read_env(
    env_file=os.path.join(BASE_DIR, '.env')
)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = read_secret("DJANGO_SECRET_KEY")
MY_REST_API_KEY = read_secret("MY_REST_API_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'wolleydb',
        'USER': 'root',
        'PASSWORD': read_secret("MYSQL_PASSWORD"),
        'HOST': 'mariadb',
        'PORT': '3306',
        "OPTIONS": {"charset": "utf8mb4"},
    }
}
