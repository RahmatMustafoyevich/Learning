from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="lessons")
    title = models.CharField(max_length=255)
    order = models.PositiveIntegerField(default=1)
    video_url = models.URLField()
    content = models.TextField(blank=True)

    class Meta:
        ordering = ["order"]
        unique_together = ("course", "order")

    def __str__(self) -> str:
        return f"{self.course.title} - {self.title}"


class LessonComment(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.user} ({self.lesson})"


class LessonRating(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name="ratings")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    stars = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    class Meta:
        unique_together = ("lesson", "user")


class Quiz(models.Model):
    lesson = models.OneToOneField(Lesson, on_delete=models.CASCADE, related_name="quiz")
    title = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.title


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name="questions")
    text = models.CharField(max_length=255)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="choices")
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)
