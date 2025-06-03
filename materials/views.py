from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, TemplateView, DetailView, CreateView, UpdateView, DeleteView
from rest_framework.views import APIView

from materials.forms import CourseForm, LessonForm
from materials.models import Course, Lesson
from rest_framework.response import Response
from django.shortcuts import render

from materials.serializers import CourseSerializer, LessonSerializer


class MainView(TemplateView):
    template_name = 'main_page.html'


class ContactView(TemplateView):
    template_name = 'contacts.html'

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        
        # Здесь можно добавить отправку email или сохранение сообщения в базу данных
        print(f"Получено сообщение от {name} (телефон: {phone}): {message}")
        
        return render(request, self.template_name, {'success': True})


class CourseListView(ListView):
    model = Course
    template_name = 'courses/courses_list.html'
    context_object_name = 'courses'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lesson_id'] = list(Lesson.objects.all())
        return context


class CourseDetailView(DetailView):
    model = Course
    template_name = 'courses/course_detail.html'
    context_object_name = 'course'

    def get_object(self, queryset=None):
        self.course = super().get_object(queryset)
        return self.course

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        course = self.get_object()
        lessons = Lesson.objects.filter(course=course)
        context['lessons'] = lessons
        return context


class CourseCreateView(CreateView):
    model = Course
    form_class = CourseForm
    success_url = reverse_lazy('materials:all_courses')
    template_name = 'courses/course_form.html'


class CourseUpdateView(UpdateView):
    model = Course
    form_class = CourseForm
    template_name = 'courses/course_form.html'

    def get_success_url(self):
        return reverse_lazy('materials:course_detail', kwargs={'pk': self.object.pk})


class CourseDeleteView(DeleteView):
    model = Course
    template_name = 'courses/course_confirm_delete.html'
    context_object_name = 'course'
    success_url = reverse_lazy('materials:all_courses')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Удаление курса'
        return context


class LessonDetailView(DetailView):
    model = Lesson
    template_name = 'lessons/lesson_detail.html'
    context_object_name = 'lesson'

    def get_object(self, queryset=None):
        self.lesson = super().get_object(queryset)
        return self.lesson


class LessonCreateView(CreateView):
    model = Lesson
    form_class = LessonForm
    template_name = 'lessons/lesson_form.html'

    def get_success_url(self):
        return reverse_lazy('materials:course_detail', kwargs={'pk': self.object.course.pk})


class LessonUpdateView(UpdateView):
    model = Lesson
    form_class = LessonForm
    template_name = 'lessons/lesson_form.html'

    def get_success_url(self):
        return reverse_lazy('materials:lesson_detail', kwargs={'pk': self.object.pk})


class LessonDeleteView(DeleteView):
    model = Lesson
    template_name = 'lessons/lesson_confirm_delete.html'
    context_object_name = 'lesson'

    def get_success_url(self):
        return reverse_lazy('materials:course_detail', kwargs={'pk': self.object.course.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Удаление урока'
        return context
