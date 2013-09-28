DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'optimal',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        #'USER': 'postgres',
        'PASSWORD': '',
        'HOST': '127.0.0.1',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}