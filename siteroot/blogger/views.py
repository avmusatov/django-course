from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Blog, Post


def get_blog_list(request):
    blogs = Blog.objects.order_by('-created_at')
    context = {'blogs': blogs}

    return render(request, 'blogger/index.html', context)


def blog(request, blog_id):
    if request.method == 'POST':
        return create_post(request, blog_id)
    else:
        return render_blog(request, blog_id)


def render_blog(request, blog_id, additional_context = {}):
    blog = get_object_or_404(Blog, id=blog_id)
    
    context = {
        'blog': blog,
        'posts': blog.post_set.order_by('-created_at'),
        **additional_context
    }

    return render(request, 'blogger/blog.html', context)


def create_post(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)

    subject = request.POST['subject']
    subject_error = None
    if not subject or subject.isspace():
        subject_error = 'Please provide non-empty subject'

    text = request.POST['text']
    text_error = None
    if not text or text.isspace():
        text_error = 'Please provide non-empty text'

    if subject_error or text_error:
        error_context = {
            'subject_error': subject_error,
            'text_error': text_error,
            'subject': subject,
            'text': text
        }
        return render_blog(request, blog_id, error_context)
    else:
        Post(blog_id=blog.id, subject=subject, text=text).save()
        return HttpResponseRedirect(reverse('blog_by_id', kwargs={ 'blog_id' : blog.id }))