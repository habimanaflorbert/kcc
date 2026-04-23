from rest_framework import serializers
from accounts.models import User

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
        return attrs


    def create(self,validated_data):
        re_enter_password=validated_data.pop("re_enter_password")
        user=User.objects.create_user(**validated_data)
        return user
        
        
    