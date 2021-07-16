from django.apps import AppConfig


class MenuConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core.menu"
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
            },
        },
        'loggers': {
            'django.request': {
                'handlers': ['console'],
                'level': 'DEBUG',  # change debug level as appropiate
                'propagate': False,
            },
        },
    }
