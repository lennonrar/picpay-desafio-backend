DEBUG = True
ALLOWED_HOSTS = ['*']

CORS_ORIGIN_ALLOW_ALL = True


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "developer",
        "USER": "admin",
        "PASSWORD": "@dm1n",
        "HOST": "postgres-container",
        "POST": "5432",
    }
}
