from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .models import BlogLike, BlogPost


def blog_list(request):
    posts = BlogPost.objects.filter(is_published=True).select_related("author")
    return render(request, "blog/list.html", {"posts": posts})


@login_required
def like_post(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id, is_published=True)
    BlogLike.objects.get_or_create(post=post, user=request.user)
    return redirect("blog:list")
