from django.shortcuts import render
from .models import Post


# Create your views here.


def home(request):
    context = {"posts": Post.objects.all()}
    return render(request, "cabin_home/home.html", context=context)


def about(request):
    return render(request, "cabin_home/about.html", {"title": "About"})
