from allauth.account.adapter import get_adapter
from rest_auth.models import TokenModel
from rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model

from apis.models import CustomUser, Contacts

UserModel = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username','email', 'phone']


class MyCustomTokenSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = TokenModel
        fields = ('key', 'user')

    class Meta:
        model = TokenModel
        fields = ('key', 'user')

    def get_user_detail(self, obj):
        serializer_data = UserSerializer(
            obj.user
        ).data
        return {
            'data': serializer_data,
        }



class CustomRegisterSerializer(RegisterSerializer):
    email = serializers.EmailField(required=True)




    class Meta:
        model = CustomUser
        fields = ('name','email','phone', 'address')


    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'password2': self.validated_data.get('password2', ''),
            'email': self.validated_data.get('email', ''),
            'phone': self.validated_data.get('phone', ''),
            'address': self.validated_data.get('address', ''),
        }

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        user.phone = self.cleaned_data.get('phone')
        user.address = self.cleaned_data.get('address')
        user.save()
        adapter.save_user(request, user, self)
        return user





class CustomuserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = "__all__"



class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = "__all__"



