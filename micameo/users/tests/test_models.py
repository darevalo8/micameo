import pytest

from micameo.users.tests.factories import (
    CategoryFactory,
    SubCategoryFactory,
    TalentFactory,
    ClientFactory
)
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


def test_sub_category__str__():
    sub_category = SubCategoryFactory()

    assert sub_category.__str__() == sub_category.sub_name
    assert str(sub_category) == sub_category.sub_name


def test_talent__str__():
    talent = TalentFactory()
    assert talent.__str__() == talent.user.__str__()
    assert str(talent) == talent.user.__str__()


def test_client__str__():
    client = ClientFactory()
    assert client.__str__() == client.user.__str__()
    assert str(client) == client.user.__str__()
