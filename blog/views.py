from django.shortcuts import get_object_or_404, render
from .models import Post
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Post
from .forms import BlogForm
from django.contrib.auth.models import User

# Create your views here.

def blog_list(request):
    posts = Post.objects.all()
    context = {
        'post_list': posts
    }
    return render(request, "blog_list.html", context)

def blog_detail(request, post_id):
    each_post = Post.objects.get(post_id=post_id)
    context = {
        'blog_detail': each_post
    }
    return render(request, "blog_detail.html", context)


def blog_delete(request , post_id) :
    each_post = Post.objects.get(post_id=post_id)
    each_post.delete()
    return HttpResponseRedirect("/blog/posts/")

def blog_create(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False) 
            post.likes = 0 
            post.edited = False
            post.save()  
            return redirect('blog_list')
    else:
        form = BlogForm()

    users = User.objects.all()
    context = {'form': form, 'users': users}
    return render(request, "blog_create.html", context)

def blog_edit(request, post_id):
    post = get_object_or_404(Post, post_id=post_id)

    if request.method == 'POST':
        form = BlogForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.edited = True 
            post.save()
            return redirect('blog_detail', post_id=post.post_id)
    else:
        form = BlogForm(instance=post)

    context = {'form': form, 'post': post}
    return render(request, 'blog_edit.html', context)