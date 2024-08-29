from django.urls import path

from materials.apps import MaterialsConfig
from rest_framework.routers import DefaultRouter

from materials.views import CourseViewSet, LessonCreateAPIView, LessonListView, LessonRetrieveAPIView, \
    LessonUpdateAPIView, LessonDestroyAPIView, SubscriptionAPIView

app_name = MaterialsConfig.name

router = DefaultRouter()
router.register(r"course", CourseViewSet, basename='course')

urlpatterns = [
    path('lesson/create/', LessonCreateAPIView.as_view(), name='create-lesson'),
    path('lesson/', LessonListView.as_view(), name='list-lesson'),
    path('lesson/<int:pk>/', LessonRetrieveAPIView.as_view(), name='get-lesson'),
    path('lesson/update/<int:pk>/', LessonUpdateAPIView.as_view(), name='update-lesson'),
    path('lesson/delete/<int:pk>/', LessonDestroyAPIView.as_view(), name='delete-lesson'),
    path('subscriptions/create/', SubscriptionAPIView.as_view(), name='create-subscription'),
] + router.urls
