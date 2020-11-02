from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class BalanceConfig(AppConfig):
    name = "micameo.balance"
    verbose_name = _("Balance")

    def ready(self):

        try:
            import micameo.balance.signals  # noqa F401
        except ImportError:
            pass
