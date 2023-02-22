from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from users.models import CustomUser
class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        user=CustomUser.objects.get(email=request.data['email'])
        
        if user.check_password(request.data['password']) :
            token,t=Token.objects.get_or_create(user=user)
            print(t,token)

            return Response({
            "message":'login successfully',
            'token': token.key,
            'userId': user.pk,
            'email': user.email
            })
        else:
            return Response({
            "message":'fail to login',
            })
