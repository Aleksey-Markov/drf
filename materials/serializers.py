from rest_framework import serializers

from materials.models import Lesson, Course


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ('title', 'description')


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = ('title', 'description')
