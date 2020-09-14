from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers

from micameo.utils.utils import ApiErrorsMixin
from micameo.order.service import create_order
from micameo.order.selectors import (get_orders_by_client, get_orders_by_talent)
from micameo.order.api.serializers import OrderSerializer


class CreateOrderApi(ApiErrorsMixin, APIView):
    class InputSerializer(serializers.Serializer):
        email_client = serializers.EmailField()
        talent = serializers.CharField()
        phone_number = serializers.CharField()
        is_public = serializers.BooleanField()
        to = serializers.CharField()
        from_client = serializers.CharField(allow_blank=True)
        occasion = serializers.CharField()
        instructions = serializers.CharField()
        order_state = serializers.IntegerField()

    def post(self, request):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        create_order(**serializer.validated_data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class OrderListClientApi(ApiErrorsMixin, APIView):

    def get(self, request):
        orders = get_orders_by_client(request.GET['email'])
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)


class OrderListTalentApi(ApiErrorsMixin, APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        orders = get_orders_by_talent(request.user)
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)
