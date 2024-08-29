from rest_framework.serializers import ModelSerializer
from rest_framework.fields import SerializerMethodField

from materials.models import Lesson, Course, Subscription
from materials.services import convert_currencies
from materials.validators import LinkValidator


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"
        validators = [LinkValidator(field='link')]


class CourseDetailSerializer(ModelSerializer):
    lessons_count = SerializerMethodField()
    lessons_info = LessonSerializer(many=True, read_only=True)
    usd_price = SerializerMethodField()

    class Meta:
        model = Course
        fields = ('title', 'description', 'lessons_count', 'lessons_info', 'usd_price')

    def get_lessons_count(self, obj):
        return obj.course.count()

    def get_usd_price(self, obj):
        return convert_currencies(obj.price)


class CourseSerializer(ModelSerializer):

    class Meta:
        model = Course
        fields = "__all__"


class SubscriptionSerializer(ModelSerializer):

    class Meta:
        model = Subscription
        fields = "__all__"
