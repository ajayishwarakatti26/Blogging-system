from django.shortcuts import render
from blogs.models import Blog, Category

def home(request):
    categories = Category.objects.all()
    # Updated status filter from "1" to "Published"
    featured_posts = Blog.objects.filter(is_featured=True, status=1).order_by('-updated_at')
    posts = Blog.objects.filter(is_featured=False, status=1)               

    context = {
        'categories': categories,
        'featured_posts': featured_posts,
        'posts': posts,
    }

    return render(request, 'home.html', context)