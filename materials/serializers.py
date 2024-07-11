from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from materials.models import Lesson, Course


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = ('title', 'description')


class CourseSerializer(serializers.ModelSerializer):
    lessons_count = serializers.SerializerMethodField()
    lessons_info = LessonSerializer(many=True, source='course')

    class Meta:
        model = Course
        fields = ('title', 'description', 'lessons_count', 'lessons_info')

    def get_lessons_count(self, obj):
        return obj.course.count()
