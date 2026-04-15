from django.contrib.auth.decorators import login_required
from django.db.models import Avg
from django.shortcuts import get_object_or_404, redirect, render

from .forms import LessonCommentForm, LessonRatingForm
from .models import Course, Lesson, LessonRating


def course_list(request):
    courses = Course.objects.filter(published=True).prefetch_related("lessons")
    return render(request, "courses/course_list.html", {"courses": courses})


def about_page(request):
    return render(request, "about.html")


@login_required
def lesson_detail(request, lesson_id):
    lesson = get_object_or_404(Lesson.objects.select_related("course"), id=lesson_id)

    if request.method == "POST" and "body" in request.POST:
        comment_form = LessonCommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.lesson = lesson
            comment.user = request.user
            comment.save()
            return redirect("courses:lesson_detail", lesson_id=lesson.id)
    else:
        comment_form = LessonCommentForm()

    rating_form = LessonRatingForm()
    average = lesson.ratings.aggregate(avg=Avg("stars"))["avg"]
    return render(
        request,
        "courses/lesson_detail.html",
        {
            "lesson": lesson,
            "comment_form": comment_form,
            "rating_form": rating_form,
            "average_rating": average,
        },
    )


@login_required
def rate_lesson(request, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id)
    form = LessonRatingForm(request.POST)
    if form.is_valid():
        LessonRating.objects.update_or_create(
            lesson=lesson,
            user=request.user,
            defaults={"stars": form.cleaned_data["stars"]},
        )
    return redirect("courses:lesson_detail", lesson_id=lesson.id)
