from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog

def get_blog_list(request):
    blogs = Blog.objects.order_by('-created_at')
    return HttpResponse(
        '<ul>'
        + ''.join(['<li> %s created ad %s </li>' % (b.title, b.created_at) for b in blogs])
        + '</ul>'
    )