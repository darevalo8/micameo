import pytest

from micameo.order.tests.factories import OccasionFactory
from micameo.order.selectors import get_occasion

pytestmark = pytest.mark.django_db


class TestOrderSelector:
    def test_get_occasion_selector(self):
        occasion = OccasionFactory(occasion_name='Cumpleaños')

        occasion_data = get_occasion("Cumpleaños")
        assert occasion_data.occasion_name == occasion.occasion_name
