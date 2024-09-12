from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView

from materials.services import create_stripe_price, create_stripe_session
from users.models import Payments, User, CoursePurchase
from users.serializers import PaymentsSerializer, MyTokenObtainPairSerializer, UserSerializer, CoursePurchaseSerializer


class PaymentsListView(ListAPIView):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['payment_type', 'payed_lesson', 'payed_course']
    ordering_fields = ['pay_date']


class CoursePurchaseCreateAPIView(CreateAPIView):

    serializer_class = CoursePurchaseSerializer
    queryset = CoursePurchase.objects.all()
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):

        purchase = serializer.save(user=self.request.user)
        price = create_stripe_price(purchase.amount)
        session_id, payment_link = create_stripe_session(price.id)
        purchase.session_id = session_id
        purchase.link = payment_link
        purchase.save()


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class UserCreateView(CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class UserListView(ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserRetrieveView(RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserUpdateView(UpdateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserDeleteView(DestroyAPIView):
    queryset = User.objects.all()

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()
