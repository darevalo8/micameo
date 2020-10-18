from micameo.users.selectors import find_talent_by_username, find_sub_category
from micameo.users.models import Talent


def update_talent(username: str, **kwargs) -> Talent:
    talent = find_talent_by_username(username)
    list_of_categories = []
    talent.response_days = kwargs['response_days']
    talent.phone_number = kwargs['phone_number']
    talent.price = kwargs['price']
    talent.profile_image = kwargs['profile_image']
    talent.description = kwargs['description']
    talent.birthday = kwargs['birthday']

    for sub_category in kwargs['categories']:
        list_of_categories.append(find_sub_category(sub_category))

    talent.categories.set(list_of_categories)
    talent.full_clean()
    talent.save()
    return talent
