from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from .models import *


def blogs(request):
    blogs_ = Blog.objects.all()
    paginator = Paginator(blogs_, 9)  # Show 10 contacts per page.

    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    context = {
        "page_obj": page_obj,
        "pages": paginator.page_range,
        "page_count": paginator.num_pages,
    }
    return render(request, template_name="blogs.html", context=context)


def single_blog(request, blog_id, slug):
    blog = get_object_or_404(Blog, id=blog_id)
    context = {
        "blog": blog,
        "recent_blogs": Blog.objects.order_by('-id')[0:5],
        "replies": Reply.objects.filter(blog=blog),
    }
    return render(request, template_name="blog.html", context=context)


def blog_reply(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    if request.method == "POST":
        reply = Reply(
            blog=blog,
            author=request.POST.get('author'),
            comment=request.POST.get('comment'),
            email=request.POST.get('email')
        )
        reply.save()
        messages.success(request, "The comment has been posted successfully")
    return redirect('single_blog', blog_id, blog.slug)
