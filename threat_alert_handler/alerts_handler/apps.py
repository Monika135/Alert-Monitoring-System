from django.apps import AppConfig


class AlertsHandlerConfig(AppConfig):
    name = 'alerts_handler'

    def ready(self):
        import alerts_handler.signals
