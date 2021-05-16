from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.generics import ListAPIView
from rest_framework.exceptions import ValidationError

from user.helpers import creat_tokens
from user.models import User
from user.serializers import UserSerializer
from user.exceptions import UnprocessableEntity


@api_view(['POST'])
@permission_classes([AllowAny])
def registration(request: Request) -> Response:
    username = request.data.get('username')
    try:
        User.objects.get(username=username)
        raise UnprocessableEntity(detail='username already exists', code=status.HTTP_406_NOT_ACCEPTABLE)
    except User.DoesNotExist:
        user = User()
        user.username = username
        user.set_password(raw_password=request.data.get('password'))
        user.verified = request.data.get('verified', True)
        user.profile_pic_url = request.data.get('profile_pic_url')
        user.address = request.data.get('address')
        user.gender = request.data.get('gender', 'male')
        user.is_superuser = request.data.get('is_superuser', False)
        user.is_staff = request.data.get('is_staff', False)
        user.first_name = request.data.get('first_name', False)
        user.last_name = request.data.get('last_name', False)
        user.save()
        return Response(data={'data': UserSerializer(user).data}, status=status.HTTP_201_CREATED)


@api_view(['POST'])
@permission_classes([AllowAny])
def login(request: Request) -> Response:
    username = request.data.get('username')
    password = request.data.get('password')

    if not username or not password:
        raise ValidationError(detail='username and password if required', code=status.HTTP_400_BAD_REQUEST)
    try:
        user = User.objects.get(username__exact=username)
        if not user.check_password(raw_password=password):
            raise ValidationError(detail='invalid password', code=status.HTTP_400_BAD_REQUEST)
        access_token, refresh_token = creat_tokens(user=user)
        data = {
            'access_token': access_token,
            'refresh_token': refresh_token,
        }
        return Response(data=data, status=status.HTTP_201_CREATED)
    except User.DoesNotExist:
        raise ValidationError(detail='user not found', code=status.HTTP_404_NOT_FOUND)


class GetUsers(ListAPIView):
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)
    queryset = User.objects.filter()


@api_view(['GET'])
@permission_classes([AllowAny])

def refreshed_token(request: Request) -> Response:
    if not request.user.is_active:
        raise ValidationError(detail='user is not active', code=status.HTTP_401_UNAUTHORIZED)
    access_token, refresh_token = creat_tokens(user=request.user)
    data = {
        'access_token': access_token,
        'refresh_token': refresh_token,
    }
    return Response(data=data, status=status.HTTP_201_CREATED)

