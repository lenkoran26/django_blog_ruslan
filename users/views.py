from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import UserRegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from blog.settings import LOGIN_REDIRECT_URL
from django.urls import reverse


def register(request):
    # если нажали кнопку Регистрация (метод POST)
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        # проверка валидности формы
        # создание словаря с данными формы cleaned_data
        if user_form.is_valid():
            # создание объекта из заполненной формы без сохранения в БД
            new_user = user_form.save(commit=False)
            # установка пароля
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()

            context = {'title': 'Успешная регистрация', 'new_user': new_user}
            return render(request, template_name='users/register_done.html', context=context)

    user_form = UserRegistrationForm()
    context = {'title': 'Регистрация пользователя', 'register_form': user_form}
    return render(request, template_name='users/register.html', context=context)


def log_in(request):
    form = AuthenticationForm(request, data=request.POST or None)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        # аутентификация (проверка наличия пользователя и соответствия пароля)
        user = authenticate(username=username, password=password)
        if user is not None:
            # авторизация (вход и получени прав доступа, подгрузка параметров пользователя)
            login(request, user)
            url = request.GET.get('next', LOGIN_REDIRECT_URL)
            return redirect(url)
    return render(request, 'users/login.html', {'form': form})



def log_out(request):
    # выходим из текущей сессии
    logout(request)
    # получаем маршрут(URL) по имени маршрута
    url = reverse('main:posts')
    # перенаправляем пользователя по полученному URL
    return redirect(url)


def get_user_info(request, pk):
    user = User.objects.get(pk=pk)
    context = {'user': user}
    return render(request, "users/user.html", context=context)
