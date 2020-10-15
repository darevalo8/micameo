from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers

from micameo.utils.utils import ApiErrorsMixin
from micameo.order.service import (create_order, update_order_state,
                                   update_order_talent_response, create_cameo,
                                   update_cameo)
from micameo.order.selectors import (get_orders_by_client, get_orders_by_talent, get_cameo_by_order,
                                     get_orders_by_talent_accept, get_cameo_by_client,
                                     get_orders_pending_and_completed)
from micameo.order.api.serializers import OrderSerializer

from micameo.utils.utils import inline_serializer


class CreateOrderApi(ApiErrorsMixin, APIView):
    class InputSerializer(serializers.Serializer):
        id = serializers.IntegerField(read_only=True)
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
        order_response = create_order(**serializer.validated_data)
        serializer_response = self.InputSerializer(order_response)
        return Response(serializer_response.data, status=status.HTTP_201_CREATED)

    def put(self, request, pk):
        order_response = update_order_state(pk, request.data['order_state'])
        serializer_response = self.InputSerializer(order_response)
        return Response(serializer_response.data, status=status.HTTP_200_OK)


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

    def put(self, request, pk):
        order_response = update_order_talent_response(pk, request.data['order_response'])
        serializer_response = OrderSerializer(order_response)
        return Response(serializer_response.data, status=status.HTTP_200_OK)


class OrderAcceptListTalentApi(ApiErrorsMixin, APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        orders = get_orders_by_talent_accept(request.user)
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)


class CreateCameoApi(ApiErrorsMixin, APIView):
    permission_classes = [permissions.IsAuthenticated]

    class InputSerializer(serializers.Serializer):
        id = serializers.IntegerField(read_only=True)
        url_video = serializers.URLField()
        order = serializers.CharField()

    def get(self, request, pk):
        cameo_response = get_cameo_by_order(pk)
        serializer_response = self.InputSerializer(cameo_response)
        return Response(serializer_response.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        cameo_response = create_cameo(**serializer.validated_data)
        serializer_response = self.InputSerializer(cameo_response)
        return Response(serializer_response.data, status=status.HTTP_201_CREATED)

    def put(self, request, pk):
        cameo_response = update_cameo(pk, request.data['url_video'])
        serializer_response = self.InputSerializer(cameo_response)
        return Response(serializer_response.data, status=status.HTTP_200_OK)


class GetCameoClientApi(ApiErrorsMixin, APIView):
    permission_classes = [permissions.IsAuthenticated]

    class OutputSerializer(serializers.Serializer):
        id = serializers.IntegerField(read_only=True)
        url_video = serializers.URLField()
        order = serializers.CharField()

    def get(self, request):
        cameo_response = get_cameo_by_client(request.user.email)
        serializer_response = self.OutputSerializer(cameo_response, many=True)
        return Response(serializer_response.data, status=status.HTTP_200_OK)


class GetTotalOrdersPendingAndCompleteApi(ApiErrorsMixin, APIView):
    permission_classes = [permissions.IsAuthenticated]

    @staticmethod
    def get(request):
        order_data = get_orders_pending_and_completed(request.user)
        fields = {
            'ordenes_pendientes': serializers.IntegerField(),
            'odenes_completadas': serializers.IntegerField(),
        }
        serializer = inline_serializer(fields=fields, data=order_data)
        serializer.is_valid()
        return Response(serializer.data, status=status.HTTP_200_OK)
