from django.contrib import admin

from .models import Choice, Course, Lesson, LessonComment, LessonRating, Question, Quiz

admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(LessonComment)
admin.site.register(LessonRating)
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Choice)
