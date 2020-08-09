from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.utils.translation import ugettext_lazy as _
from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from micameo.users.api.serializers import UserSerializer
from micameo.users.tasks import send_email
from micameo.users.token_generator import account_activation_token


class RegisterUser(APIView):
    model = None
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        email = request.data['email']
        index = email.find("@")
        data_user = {
            'username': email[0:index],
            'password': request.data['password'],
            'email': request.data['email']
        }
        user_serializer = UserSerializer(data=data_user)
        if user_serializer.is_valid():
            user = user_serializer.save()
            profile = self.model(user=user)
            profile.save()
            current_site = get_current_site(request)
            message = render_to_string('acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            send_email.delay(message, data_user['email'])
            message = {'message': _("Usuario registrado exitosamente")}
            return Response(message, status=status.HTTP_201_CREATED)
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
