from django.shortcuts import render
from .forms import UserRegister
from django.http import HttpResponse
# Create your views here.

users = ['Pasha Technique', 'Valera', 'Batman']

def sign_up_by_django(request):
    info = {}
    form = UserRegister()

    if request.method == 'POST':
        form = UserRegister(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            if username in users:
                info['error'] = 'Пользователь уже существует'
            elif password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif age < 18:
                info['error'] = 'Вы должны быть старше 18'
            elif age > 120:  # Добавлена проверка на верхний предел
                info['error'] = 'Ваш возраст не может быть больше 120 лет'
            else:
                return render(request, 'fifth_task/registration_page.html',
                              {'message': f'Приветствуем, {username}!'})
        else:
            info['form'] = form
    info['form'] = form
    return render(request, 'fifth_task/registration_page.html', info)


def sign_up_by_html(request):
    info = {}

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = int(request.POST.get('age', 0))

        if username in users:  # Проверки на валидность
            info['error'] = 'Пользователь уже существует'
        elif password != repeat_password:
            info['error'] = 'Пароли не совпадают'
        elif age < 18:
            info['error'] = 'Вы должны быть старше 18'
        elif age > 120:  # Добавлена проверка на верхний предел
            info['error'] = 'Ваш возраст не может быть больше 120 лет'
        else:
            info['message'] = f'Приветствуем, {username}!'

            return render(request, 'fifth_task/registration_page1.html', info)

    return render(request, 'fifth_task/registration_page1.html', info)