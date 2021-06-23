from django.shortcuts import render , get_object_or_404
from .models import Blog

def all_blogs(request):
    blog = Blog.objects.all()
    return render(request , 'blog.html' , {'blogs': blog})

def detail(request,blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request , 'detail.html' , {'blog': blog})    
