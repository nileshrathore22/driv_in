from django.shortcuts import render
from .models import Post, Category

def blog_list(request):
    categories = Category.objects.all()
    posts = Post.objects.all().order_by('-datetime_post')
    return render(request, 'blog.html', {'categories': categories, 'posts': posts})
