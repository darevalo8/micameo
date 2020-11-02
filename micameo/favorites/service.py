from micameo.favorites.models import Favorite
from micameo.users.selectors import find_client_by_username, find_talent_by_username


def create_favorito(username: str, talent: str) -> Favorite:
    talent = find_talent_by_username(talent)
    client = find_client_by_username(username)
    favorte = Favorite(client=client, talent=talent)
    favorte.full_clean()
    favorte.save()
    return Favorite


def delete_favorite(pk):
    Favorite.objects.get(pk=pk).delete()
