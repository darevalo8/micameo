from django.apps import AppConfig


class OrderConfig(AppConfig):
    name = 'micameo.order'

    def ready(self):

        try:
            import micameo.order.signals  # noqa F401
        except ImportError:
            pass
