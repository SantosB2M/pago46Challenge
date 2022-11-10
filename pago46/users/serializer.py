from rest_framework import serializers
from users.models import User
from finance.serializer import IOUSerializer

class UserIOUSerializer(serializers.ModelSerializer):
    lent = IOUSerializer(many=True, source='borrowed')
    borrows = IOUSerializer(many=True, source= 'lent')
    class Meta:
        model = User
        fields = ["last_name", "lent","borrows"]

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["last_name"]
