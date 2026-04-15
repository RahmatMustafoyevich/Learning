from django.shortcuts import render

from .models import Resource


def resource_list(request):
    items = Resource.objects.all()
    return render(request, "resources/list.html", {"items": items})
