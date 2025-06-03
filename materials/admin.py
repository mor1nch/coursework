from django.contrib import admin

from materials.models import Course, Lesson


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'create_date',
                    'image', 'owner')
    list_filter = ('title', 'create_date')


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'video',
                    'course', 'owner', 'text', 'image')
    list_filter = ('title', 'course')
