from micameo.favorites.models import Favorite
from micameo.users.models import Client


def get_favorites(client:str) -> Favorite:
    favorites = Favorite.objects.filter(client__slug=client)
    return favorites
