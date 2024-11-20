from django.shortcuts import render, redirect
from .forms import UserRegister
from .models import Game


# Create your views here.

def home(request):
    return render(request, 'home.html')


def get_shop(request):
    games = Game.objects.all()
    return render(request, 'shop.html', {"games": games})


def get_basket(request):
    return render(request, 'basket.html')


users = []


def sign_up_by_django(request):
    return process_registration(request)


def sign_up_by_html(request):
    return process_registration(request)


from .models import Buyer


def process_registration(request):
    info = {}
    if request.method=='POST':
        form = UserRegister(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            if Buyer.objects.filter(name=username).exists():
                info['error'] = 'Пользователь уже существует'
            if password!=repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif int(age) < 18:
                info['error'] = 'Вы должны быть старше 18'
            elif username in users:
                info['error'] = 'Пользователь уже существует'
            else:
                Buyer.objects.create(name=username, balance=0, age=age)
                info['success_message'] = f'Вы зарегистрированы, {username}!'
        else:
            info['error'] = 'Пожалуйста, исправьте ошибки в форме.'
    else:
        form = UserRegister()

    info['form'] = form
    return render(request, 'registration_page.html', info)
# Create your views here.
