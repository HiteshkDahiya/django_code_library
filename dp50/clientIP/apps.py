from django.apps import AppConfig


class ClientipConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'clientIP'

    def ready(self):
        import clientIP.signals