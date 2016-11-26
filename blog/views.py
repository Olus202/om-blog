from django.shortcuts import render, get_object_or_404

from blog.models import Post


def home_page(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})


def post_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_view.html', {'post': post})


def all_posts(request):
    posts = Post.objects.all()
    return render(request, 'all_posts.html', {'posts': posts})


def polish_crown(request):
    posts = Post.objects.all()
    return render(request, 'polish_crown.html', {'posts': posts})

