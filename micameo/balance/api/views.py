from rest_framework import permissions
from rest_framework import serializers
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from micameo.balance.models import BalanceTalent, Withdraw
from micameo.balance.selectors import get_balance_talent, get_withdraws
from micameo.users.selectors import find_talent_by_username
from micameo.utils.utils import ApiErrorsMixin
from micameo.balance.service import add_withdraw


class GetBalanceTalentApi(ApiErrorsMixin, APIView):
    permission_classes = [permissions.IsAuthenticated]

    class OutputSerializer(serializers.ModelSerializer):
        class Meta:
            model = BalanceTalent
            fields = "__all__"

    def get(self, request):
        talent = find_talent_by_username(request.user.username)
        balance = get_balance_talent(talent=talent)
        serializer_response = self.OutputSerializer(balance)
        return Response(serializer_response.data, status=status.HTTP_200_OK)


class WithdrawApi(ApiErrorsMixin, APIView):
    permission_classes = [permissions.IsAuthenticated]

    class OutputSerializer(serializers.ModelSerializer):
        class Meta:
            model = Withdraw
            fields = "__all__"

    def get(self, request):
        talent = find_talent_by_username(request.user.username)
        balance = get_balance_talent(talent=talent)
        withdraw = get_withdraws(balance_talent=balance)
        serializer_response = self.OutputSerializer(withdraw, many=True)
        return Response(serializer_response.data, status=status.HTTP_200_OK)

    def post(self, request):
        talent = find_talent_by_username(request.user.username)
        balance = get_balance_talent(talent=talent)
        withdraw = add_withdraw(balance, amount=request.data["amount"])
        serializer_response = self.OutputSerializer(withdraw)
        return Response(serializer_response.data, status=status.HTTP_201_CREATED)
