from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from materials.models import Lesson, Course, Subscription
from materials.validators import LinkValidator


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = ('title', 'description')
        validators = [LinkValidator(field='link')]


class CourseSerializer(serializers.ModelSerializer):
    lessons_count = serializers.SerializerMethodField()
    lessons_info = LessonSerializer(many=True, source='course')

    class Meta:
        model = Course
        fields = ('title', 'description', 'lessons_count', 'lessons_info')

    def get_lessons_count(self, obj):
        return obj.course.count()


class SubscriptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subscription
        fields = "__all__"
