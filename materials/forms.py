from django.forms import ModelForm

from materials.models import Course, Lesson


class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = ('title', 'description', 'image', 'course_topics')


class LessonForm(ModelForm):
    class Meta:
        model = Lesson
        fields = ('title', 'description', 'video', 'course', 'owner', 'text', 'image')
