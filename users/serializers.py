from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from users.models import Payments, User, CoursePurchase


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class PaymentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payments
        fields = "__all__"


class CoursePurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoursePurchase
        exclude = ("user",)


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        token['email'] = user.email
        return token
