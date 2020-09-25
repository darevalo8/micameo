from rest_framework import serializers
from micameo.order.models import Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"

    talent = serializers.StringRelatedField(read_only=True)
    occasion = serializers.StringRelatedField(read_only=True)
    pay_method = serializers.CharField(source='get_pay_method_display')
    talent_response = serializers.CharField(source='get_talent_response_display')
    order_state = serializers.CharField(source='get_order_state_display')
