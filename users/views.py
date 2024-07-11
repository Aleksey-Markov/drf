from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView

from users.models import Payments
from users.serializers import PaymentsSerializer


class PaymentsListView(ListAPIView):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['payment_type', 'payed_lesson', 'payed_course']
    ordering_fields = ['pay_date']
