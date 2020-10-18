from micameo.users.models import Talent, SubCategory
from django.core.exceptions import ValidationError


def find_talent_by_username(username: str) -> Talent:
    try:
        talent = Talent.objects.get(user__username=username)
    except Talent.DoesNotExist:
        raise ValidationError("Este talento no existe")
    return talent


def find_sub_category(sub_name: str) -> SubCategory:
    try:
        sub_category = SubCategory.objects.get(sub_name=sub_name)
    except SubCategory.DoesNotExist:
        raise ValidationError("Esta SubCategoria no existe")
    return sub_category
