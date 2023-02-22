from .models import CustomUser
from rest_framework import serializers


class UserSerializer (serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'userId','last_name', 'password', 'contact_no',
                 'profilePic', 'address']


