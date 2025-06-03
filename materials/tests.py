from django.urls import reverse, reverse_lazy
from django.test import TestCase, Client
from rest_framework import status

from materials.models import Course, Lesson
from users.models import User


class CourseTestCase(TestCase):
    def setUp(self):
        # Создаем тестового пользователя
        self.user = User.objects.create(
            email='testuser@gmail.com',
            password='password123',
            is_active=True,
            verification_code='12345678'
        )
        self.user.set_password('password123')
        self.user.save()
        self.course1 = Course.objects.create(owner=self.user, title="Test Course 1", description="description",
                                             course_topics="1, 2, 3", image='media/courses/history.jpeg',
                                             create_date='2024-08-05')
        self.course2 = Course.objects.create(owner=self.user, title="Test Course 2", description="description",
                                             course_topics="1, 2, 3", image='media/courses/history.jpeg',
                                             create_date='2024-08-05')
        self.course_data = {
            'title': 'Test Course',
            'description': 'Description of the test course',
            'course_topics': 'Topic 1, Topic 2',
            'owner': self.user.id,
            'create_date': '2024-08-05',
            'course': self.course1.pk}

        # Создаем клиент
        self.client = Client()
        self.client.login(email='testuser@gmail.com', password='password123')

    def test_get_courses(self):
        url = reverse_lazy('materials:all_courses')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_course(self):
        url = reverse_lazy('materials:course_update', kwargs={'pk': self.course1.pk})
        data = {
            'title': 'Updated Test Course',
            'description': 'Updated description of the test course',
            'course_topics': 'Updated Topic 1, Updated Topic 2',
            'owner': self.user.id,
            'create_date': '2024-08-05',
            'course': self.course1.pk
        }
        response = self.client.put(url, data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class LessonTestCase(TestCase):
    def setUp(self):
        # Создаем тестового пользователя
        self.user = User.objects.create(
            email='testuser@gmail.com',
            password='password123',
            is_active=True,
            verification_code='12345678'
        )
        self.user.set_password('password123')
        self.user.save()

        # Создаем тестовый курс
        self.course = Course.objects.create(title='Test Course', owner=self.user)

        # Создаем тестовые уроки
        self.lesson1 = Lesson.objects.create(title='Lesson 1', course=self.course,
                                             description='-', video='https://www.youtube.com/', text='-',
                                             owner=self.user)
        self.lesson2 = Lesson.objects.create(title='Lesson 2', course=self.course,
                                             description='-', video='https://www.youtube.com/', text='-',
                                             owner=self.user)

        # Создаем клиент
        self.client = Client()
        self.client.login(email='testuser@gmail.com', password='password123')

    def test_retrieve_lesson(self):
        url = reverse('materials:lesson_detail', kwargs={'pk': self.lesson1.pk})
        response = self.client.get(url, HTTP_ACCEPT='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_lesson(self):
        url = reverse('materials:lesson_update', kwargs={'pk': self.lesson1.pk})
        data = {'title': 'New Lesson is updated', 'course': self.course.id,
                'video': 'https://www.youtube.com/', 'description': '---', 'text': '-',
                'owner': self.user.id}
        response = self.client.put(url, data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
