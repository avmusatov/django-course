from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Blog
from django.template import loader
from django.shortcuts import get_object_or_404

def get_blog_list(request):
    blogs = Blog.objects.order_by('-created_at')
    template = loader.get_template('blogger/index.html')
    context = {'blogs': blogs}
    return HttpResponse(template.render(context, request))


def get_blog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    template = loader.get_template('blogger/blog.html')
    context = {'blog': blog}
    return HttpResponse(template.render(context, request))