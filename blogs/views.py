from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Blog,Category
from django.shortcuts import get_object_or_404


# Create your views here.
def posts_by_category(request,category_id):
    posts=Blog.objects.filter(status="1", category=category_id)
    try:
         category=Category.objects.get(pk=category_id)
    except:
         return redirect('home')
         
    context={
        'posts':posts,
        'category':category,
        
    }
    return render(request,"posts_by_category.html",context)
    
