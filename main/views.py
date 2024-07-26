from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseForbidden
from .forms import PostForm
from .models import Post


# Create your views here.

def index(request):
    return render(request, 'main/index.html')


def posts(request):
    title = 'Посты'
    posts = Post.objects.all()
    context = {'title': title, 'posts': posts}
    return render(request, template_name='main/posts.html', context=context)


def post_add(request):
    title = 'Добавить пост'
    if request.method == 'GET':
        form = PostForm(author=request.user)
        context = {"title": title, "form": form}
        return render(request, template_name="main/new_post.html", context=context)

    if request.method == 'POST':
        post_form = PostForm(request.POST, request.FILES, author=request.user)
        if post_form.is_valid():
            # post = Post()
            # post.author = request.user
            # post.title = post_form.cleaned_data['title']
            # post.text = post_form.cleaned_data['text']
            # post.image = post_form.cleaned_data['image']
            # post.save()
            post_form.save()
            # instance = post_form.save(commit=False)
            # #instance.author = request.user  # Сохраняем пользователя вместе с формой
            # instance.save()

            return posts(request)


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    title = "Информация о посте"
    context = {"post": post, "title": title}
    return render(request, template_name="main/post_detail.html", context=context)


def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.author != request.user:
        raise PermissionDenied

    title = "Редактирование поста"

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)

        if form.is_valid():
            form.save()
            return redirect("main:post_detail", pk=pk)

    form = PostForm(instance=post)
    context = {"form": form}
    return render(request, 'main/post_update.html', context=context)


def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.author != request.user:
        raise PermissionDenied

    post.delete()

    return redirect("main:posts")


def handle_permission_denied(request, exception):

    return HttpResponseForbidden("У вас нет прав для выполнения этой операции")



