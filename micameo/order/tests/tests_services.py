import pytest
from micameo.users.tests.factories import TalentFactory
from micameo.order.tests.factories import OccasionFactory
from micameo.order.service import create_order

pytestmark = pytest.mark.django_db


class TestOrderService:
    def test_create_order_service(self):
        talent = TalentFactory()
        occasion = OccasionFactory(occasion_name='Cumpleaños')
        # {
        #     "full_name": "Oscar",
        #     "email": "oscar@hotmail.com",
        #     "phone_number": "3104496561",
        #     "where_find_you": 1,
        #     "username": "elñato",
        #     "followers": 6000000
        # }

        data_order = {
            'email_client': 'pruebita@prueba.com',
            'talent': talent.user.username,
            'is_public': True,
            'to': 'Daniel',
            'from_client': 'Andres',
            'occasion': occasion.occasion_name,
            'phone_number': '3104496561',
            'instructions': 'perrosssssssss',
            'order_state': 2
        }
        order = create_order(**data_order)

        assert order.email_client == data_order['email_client']
