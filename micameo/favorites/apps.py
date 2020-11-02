from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class FavoritesConfig(AppConfig):
    name = "micameo.favorites"
    verbose_name = _("favorites")

    def ready(self):

        try:
            import micameo.favorites.signals  # noqa F401
        except ImportError:
            pass
