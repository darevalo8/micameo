import facebook
import tweepy
from django.conf import settings
from django.contrib.auth import get_user_model
from django.shortcuts import HttpResponse
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken

from micameo.users.api.serializers import UserSerializer, CustomTokenObtainPairSerializer
from micameo.users.token_generator import account_activation_token
from micameo.users.models import Client

User = get_user_model()


class UserViewSet(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = "username"

    @action(detail=False, methods=["GET"])
    def me(self, request):
        serializer = UserSerializer(request.user, context={"request": request})
        return Response(status=status.HTTP_200_OK, data=serializer.data)


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()

        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class LoginSocialView(APIView):

    def post(self, request):
        response = {}
        access_token = request.data['access_token']
        social_network = request.data['social_network']

        if social_network == 'twitter':
            access_token_secret = request.data['access_token_secret']
            email = request.data['email']

            try:
                auth = tweepy.OAuthHandler(settings.SOCIAL_AUTH_TWITTER_KEY, settings.SOCIAL_AUTH_TWITTER_SECRET)
                auth.set_access_token(access_token, access_token_secret)
                api = tweepy.API(auth)
                user_info = api.me()
                index = user_info.name.find(" ")
                data = {
                    'first_name': user_info.name[:index],
                    'last_name': user_info.name[index:],
                    'username': user_info.screen_name,
                    'email': email,
                    'profile_url': user_info.profile_image_url_https
                }
                response = self.get_or_create_client(data)
                print(user_info.profile_image_url_https)
            except tweepy.TweepError:
                return Response(status=status.HTTP_400_BAD_REQUEST, data={'error': "access_token invalido"})

        elif social_network == 'facebook':
            try:
                graph = facebook.GraphAPI(access_token=access_token)
                user_info = graph.get_object(
                    id='me',
                    fields='first_name, middle_name, last_name, id, '
                           'currency, hometown, location, locale, '
                           'email, gender, interested_in, picture.type(large),'
                           ' birthday, cover')

                data = {
                    'first_name': user_info['first_name'],
                    'last_name': user_info['last_name'],
                    'username': user_info['first_name'] + user_info['last_name'],
                    'email': user_info['email'],
                    'profile_url': user_info['picture']['data']['url']
                }
                response = self.get_or_create_client(data)
                print(user_info)
            except facebook.GraphAPIError:
                return Response(status=status.HTTP_400_BAD_REQUEST, data={'error': "access_token invalido"})

        refresh = RefreshToken.for_user(response['user'])
        context = {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
        return Response(status=status.HTTP_200_OK, data=context)

    @staticmethod
    def get_or_create_client(data):
        try:
            user = User.objects.get(email=data['email'])
        except User.DoesNotExist:
            password = User.objects.make_random_password()
            user = User(
                first_name=data['first_name'],
                last_name=data['last_name'],
                email=data['email'],
                username=data['username']
            )
            user.set_password(password)
            user.save()
        try:
            client = Client.objects.get(user=user)
        except Client.DoesNotExist:
            client = Client(
                user=user,
                profile_image=data['profile_url']
            )
            client.save()

        contex = {
            'user': user,
            'client': client
        }
        return contex
