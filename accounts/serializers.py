from rest_framework import serializers
from accounts.models import User, VerificationCode
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
import datetime
from utils.gencode import random_with_N_digits
from utils.sendemail import send_email

class UserSerializer(serializers.ModelSerializer):
    re_enter_password=serializers.CharField(write_only=True)
    class Meta:
        model=User
        fields=["id","email","full_name","phone_number","is_active","is_staff","is_admin","created_on","password","re_enter_password"]
        read_only_fields=["id","is_active","is_staff","is_admin","created_on"]
        extra_kwargs={
            "password":{"write_only":True}
        }
    
    def validate(self, attrs):
        if attrs['password'] != attrs['re_enter_password']:
            raise serializers.ValidationError(
                {"re_enter_password": "Passwords do not match"}
            )
        if User.objects.filter(email=attrs['email']).exists():
            raise serializers.ValidationError(
                {"email": "Email already exists"}
            )
        return attrs


    def create(self,validated_data):
        re_enter_password=validated_data.pop("re_enter_password")
        user=User.objects.create_user(**validated_data)
        ver=VerificationCode.objects.create(
            user=user,
            code=random_with_N_digits(4),
        )
        send_email(user.full_name,ver.code,"Reset Account verification code",user.email)
        return user
        

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        User.objects.filter(id=user.id).update(
            last_login=datetime.datetime.now())
        user.save()
        token = super().get_token(user)
        # Add custom claims
        token["full_name"] = user.full_name
        token["email"] = user.email
        token["phone_number"] = user.phone_number
        token["user_type"] = user.user_type
        return token
    