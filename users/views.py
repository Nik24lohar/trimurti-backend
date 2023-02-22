
from rest_framework import status
from rest_framework.authentication import TokenAuthentication,SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.exceptions import ObjectDoesNotExist
from users.models import  CustomUser 
from rest_framework import generics
from .serializers import UserSerializer as userSerializer 
from rest_framework import filters
# Create your views here.
class userAPIView(generics.UpdateAPIView):
    queryset=CustomUser.objects.all()
    serializer_class=userSerializer
    def put(self, request, *args, **kwargs):
        try:
            queryset =CustomUser.objects.filter(email=kwargs['email'])
            user=userSerializer(queryset,data=request.data)
            if user.is_valid():
                user.save()
                return Response(user.data,status=status.HTTP_202_ACCEPTED)
            return Response(user.data,status=status.HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist:
            return Response("USER RECORD NOT FOUND",status=status.HTTP_400_BAD_REQUEST)


    def patch(self, request, *args, **kwargs):
        try:
            queryset =CustomUser.objects.get(email=kwargs['email'])
            user=userSerializer(queryset,data=request.data,partial=True)
            if user.is_valid():
                user.save()
                return Response(user.data,status=status.HTTP_202_ACCEPTED)
            return Response(user.data,status=status.HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist:
            return Response("USER RECORD NOT FOUND",status=status.HTTP_400_BAD_REQUEST)

        
    def delete(self, request, *args, **kwargs):
        try:
            queryset =CustomUser.objects.get(email=kwargs['email'])
            user_data=userSerializer(queryset)
            queryset.delete()
            return Response({"deleted":user_data.data},status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response("USER RECORD NOT FOUND",status=status.HTTP_400_BAD_REQUEST)

class UserList(generics.ListCreateAPIView):
    queryset=CustomUser.objects.all()
    serializer_class=userSerializer
    def get(self, request,format = None): 
        user = CustomUser.objects.all()
        print("User", user)
        if user.count()>0:
            user_data =userSerializer(data=user,many=True)
            user_data.is_valid()
            print("User Data:",user_data.data)
            return Response({"message":"login sccessfully",'userData':user.data,"status ": status.HTTP_201_CREATED})
        return Response({"message":"fail to login",'userData':user.data,"status ": status.HTTP_400_BAD_REQUEST})
    
    def post(self, request,format = None):
        print(request.data)
        user = userSerializer(data = request.data)
        if user.is_valid():
            user.save()
            current_user = CustomUser.objects.get(email=request.data['email'])
            current_user.set_password(request.data['password'])
            current_user.is_active=True
            current_user.save()
            user = userSerializer(current_user)
            return Response({"message":"user registered sccessfully",'userData':user.data,"status ": status.HTTP_201_CREATED})
        return Response({"message":"fail to register",'userData':user.data,"status ": status.HTTP_400_BAD_REQUEST})  