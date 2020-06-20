import pytest

from micameo.users.tests.factories import CategoryFactory
from micameo.users.models import User

pytestmark = pytest.mark.django_db


def test_user_get_absolute_url(user: User):
    # user = UserFactory()
    assert user.get_absolute_url() == f"/users/{user.username}/"


def test___str__(user: User):
    # user = UserFactory()
    assert user.__str__() == user.username
    assert str(user) == user.username


def test_category__str__():
    category = CategoryFactory()

    assert category.__str__() == category.name
    assert str(category) == category.name
