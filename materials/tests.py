from rest_framework.reverse import reverse
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from materials.models import Lesson, Course, Subscription
from users.models import User


class SubscriptionsTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email="admin@admin.com")

        self.course = Course.objects.create(title='Курс номер 1', description='Описание курса номер 1',  owner=self.user)

        video = "https://www.youtube.com/watch?v=34Rp6KVGIEM&list=PLDyJYA6aTY1lPWXBPk0gw6gR8fEtPDGKa"

        self.lesson = Lesson.objects.create(title='Урок номер 1', course=self.course , description="описание" , link=video, owner=self.user)

        self.client.force_authenticate(user=self.user)

        self.subscription = Subscription.objects.create(user=self.user, course=self.course)

    def test_lesson_create(self):
        url = reverse("materials:create-lesson")

        data = {
            "title": "lesson 2",
            "course": self.course.pk
        }

        response = self.client.post(url, data)

        data = response.json()

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Lesson.objects.all().count(), 2)

    def test_lesson_update(self):
        url = reverse("materials:update-lesson", args=(self.lesson.pk,))
        data = {"title": "Updated lesson"}
        response = self.client.patch(url, data)

        data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get('title'), "Updated lesson")

    def test_lesson_delete(self):
        url = reverse("materials:delete-lesson", args=(self.lesson.pk,))
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Lesson.objects.all().count(), 0)

    def test_lesson_retrieve(self):
        url = reverse("materials:get-lesson", args=(self.lesson.pk,))
        response = self.client.get(url)
        data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get('title'), self.lesson.title)

    def test_lesson_list(self):
        url = reverse("materials:list-lesson")
        response = self.client.get(url)

        data = response.json()

        result = {'count': 1,
                  'next': None,
                  'previous': None,
                  'results':
                      [
                          {'id': self.lesson.pk,
                           'title': self.lesson.title,
                           'description': self.lesson.description,
                           'preview': None,
                           'video_url': self.lesson.video_url,
                           'course': self.lesson.course.pk,
                           'owner': self.user.pk,
                           }
                      ]
                  }

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, result)
