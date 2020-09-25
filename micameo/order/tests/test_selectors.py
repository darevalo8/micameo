import pytest
from django.core.exceptions import ValidationError

from micameo.order.selectors import (get_occasion, get_order,
                                     get_orders_by_talent, get_orders_by_client,
                                     list_occasion, get_cameo, get_cameo_by_order)
from micameo.order.tests.factories import OccasionFactory, OrderFactory, CameoFactory
from micameo.users.tests.factories import UserFactory

pytestmark = pytest.mark.django_db


class TestOrderSelector:
    def test_get_occasion_selector(self):
        occasion = OccasionFactory(occasion_name='Cumpleaños')

        occasion_data = get_occasion("Cumpleaños")
        with pytest.raises(ValidationError, match="Ocasion no existe"):
            get_occasion("Cumpleaño")
        assert occasion_data.occasion_name == occasion.occasion_name

    def test_get_list_occasion(self):
        OccasionFactory()
        occasion_data = list_occasion()
        assert occasion_data.count() >= 1

    def test_get_orders(self):
        order = OrderFactory()
        order_data = get_order(order.pk)
        with pytest.raises(ValidationError, match="Order does no exist"):
            get_order(3)
        assert order_data.pk == order.pk

    def test_get_cameo(self):
        cameo = CameoFactory()
        cameo_data = get_cameo(cameo.pk)
        with pytest.raises(ValidationError, match="Cameo does no exist"):
            get_cameo(3)
        assert cameo_data.pk == cameo.pk

    def test_get_cameo_by_order(self):
        cameo = CameoFactory()
        cameo_data = get_cameo_by_order(cameo.order.id)
        with pytest.raises(ValidationError, match="Cameo does no exist"):
            get_cameo_by_order(3)
        assert cameo_data.order_id == cameo.order_id

    def test_get_orders_by_talents(self):
        user = UserFactory()
        order = OrderFactory(order_state=2)
        order_data = get_orders_by_talent(order.talent.user)
        order_data_two = get_orders_by_talent(user=user)
        assert order_data.count() >= 1
        assert order_data_two.count() == 0

    def test_get_orders_by_client(self):
        order = OrderFactory()
        order_data = get_orders_by_client(order.email_client)
        order_data_two = get_orders_by_client("prueba@prueba.com")
        assert order_data.count() >= 1
        assert order_data_two.count() == 0
