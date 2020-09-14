from micameo.users.models import Talent
from django.core.exceptions import ValidationError


def find_talent_by_username(username: str) -> Talent:
    try:
        talent = Talent.objects.get(user__username=username)
    except Talent.DoesNotExist:
        raise ValidationError("Este talento no existe")
    return talent
