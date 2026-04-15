from django import forms

from .models import LessonComment, LessonRating


class LessonCommentForm(forms.ModelForm):
    class Meta:
        model = LessonComment
        fields = ("body",)


class LessonRatingForm(forms.ModelForm):
    class Meta:
        model = LessonRating
        fields = ("stars",)
