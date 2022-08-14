# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '{{django_secret_key}}'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# TODO poll.iccmeurope.org?
ALLOWED_HOSTS = ["{{domain}}", "{{domain2}}", "{{pac}}.hostsharing.net", "127.0.0.1"]
CSRF_TRUSTED_ORIGINS = ["{{domain}}", "{{domain2}}"]

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('redis://:{{redispassword}}@127.0.0.1:{{redisport}}')]
        },
    },
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '{{pac}}_{{user}}',
        'USER': '{{pac}}_{{user}}',
        'PASSWORD': '{{password}}',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}