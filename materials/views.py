from django.shortcuts import get_object_or_404
from rest_framework import viewsets, generics
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action

from materials.models import Lesson, Course, Subscription
from materials.paginators import MyPagination
from materials.serializers import CourseSerializer, LessonSerializer, SubscriptionSerializer, CourseDetailSerializer
from users.permissions import IsModer, IsOwner
from materials.tasks import sending


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    permission_classes = [IsModer | IsOwner]

    def get_serializer_class(self):
        if self.action == "retrieve":
            return CourseDetailSerializer
        return CourseSerializer

    # def sending(self):
    #     if self.request.method == "POST":
    #         sending.delay()


class LessonCreateAPIView(CreateAPIView):
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        new_lesson = serializer.save()
        new_lesson.owner = self.request.user
        new_lesson.save()


class LessonListView(ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsModer]


class LessonRetrieveAPIView(RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsModer | IsOwner]


class LessonUpdateAPIView(UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsModer]

    def sss(self):
        if self.request.method == "PUT":
            sending.delay()


class LessonDestroyAPIView(DestroyAPIView):
    queryset = Lesson.objects.all()
    permission_classes = [IsOwner]


class SubscriptionAPIView(CreateAPIView):
    serializer_class = SubscriptionSerializer
    pagination_class = MyPagination

    def get(self, request):
        queryset = Subscription.objects.all()
        paginated_queryset = self.paginate_queryset(queryset)
        serializer = SubscriptionSerializer(paginated_queryset, many=True)
        return self.get_paginated_response(serializer.data)

    def post(self, *args, **kwargs):
        user = self.request.user
        course_id = self.request.data.get('course')
        course_item = get_object_or_404(Course, pk=course_id)

        subscription, created = Subscription.objects.get_or_create(user=user, course=course_item)
        if not created:
            subscription.delete()
            message = 'Подписка удалена'
        else:
            message = 'Подписка подключена'

        return Response({"message": message})
