from rest_framework import permissions
from rest_framework import serializers
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from micameo.utils.utils import ApiErrorsMixin
from micameo.favorites.models import Favorite
from micameo.favorites.selectors import get_favorites
from micameo.favorites.service import create_favorito, delete_favorite
from micameo.users.api.serializers import TalentSerializer


class FavoriteApi(ApiErrorsMixin, APIView):
    permission_classes = [permissions.IsAuthenticated]

    class OutPutSerializer(serializers.ModelSerializer):
        talent = TalentSerializer(read_only=True)

        class Meta:
            model = Favorite
            fields = "__all__"

    def get(self, request):
        favorites = get_favorites(request.user.username)
        serializer = self.OutPutSerializer(favorites, many=True, context={'request': request})
        return Response(serializer.data)

    @staticmethod
    def post(request):
        create_favorito(request.user.username, talent=request.data['talent'])
        return Response(status=status.HTTP_201_CREATED)

    @staticmethod
    def delete(request, pk):
        delete_favorite(pk)
        return Response(status=status.HTTP_200_OK)
