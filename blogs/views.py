from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog


# Create your views here.
def posts_by_category(request,category_id):
    posts=Blog.objects.filter(status="1", category=category_id)
    context={
        'posts':posts,
    }
    return render(request,"posts_by_category.html",context)
    
