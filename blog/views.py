from django.shortcuts import render, get_object_or_404

from blog.models import Post


def home_page(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})


def post_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_view.html', {'post': post})
