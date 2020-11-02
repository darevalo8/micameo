from rest_framework import permissions
from rest_framework import serializers
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from micameo.balance.models import BalanceTalent
from micameo.balance.selectors import get_balance_talent
from micameo.users.selectors import find_talent_by_username
from micameo.utils.utils import ApiErrorsMixin


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
