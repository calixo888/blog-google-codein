from django.shortcuts import render
from django.http import HttpResponseRedirect
from . import models
import datetime

def index(request):
    posts = models.BlogPost.objects.all()
    return render(request, "index.html", context={"posts": posts})

def add(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        date = datetime.date.today()

        post = models.BlogPost(title=title, content=content, date=date)
        post.save()

        return HttpResponseRedirect("/")

    return render(request, "add.html")
