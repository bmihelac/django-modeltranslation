DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'example.db',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

LANGUAGE_CODE = 'en-us'

LANGUAGES = (
    ('en', 'English'),
    ('pl', 'Polish'),
)

SITE_ID = 1

USE_I18N = True

# Make this unique, and don't share it with anybody.
SECRET_KEY = '!ut&+go##_4p&hj#ao@0mk95v%vux^2y$m=iqfqk(xloi*!)0n'

TEMPLATE_CONTEXT_PROCESSORS = (
'django.core.context_processors.auth',
'django.core.context_processors.debug',
'django.core.context_processors.i18n',
'multilingual.context_processors.multilingual',
)

ROOT_URLCONF = 'example.urls'

TRANSLATION_REGISTRY = "example.translation"

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    
    'modeltranslation',
    
    'example',
    
)
