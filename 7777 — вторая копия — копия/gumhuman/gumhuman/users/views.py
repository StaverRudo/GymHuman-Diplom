from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from django.urls import reverse

from users.models import User
from users.forms import UserLoginForm, UserRegistrationForm
from articles.models import Article
from django.contrib.auth import logout
from django.shortcuts import redirect
from .forms import TrainingForm
from .models import TrainingRecord



def logout_view(request):
    logout(request)
    return redirect('index')


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('articles:about'))
    else:
        form = UserLoginForm()
    context = {'form': form}
    return render(request, 'users/login.html', context)

# def registration(request):
#     if request.method == 'POST':
#         form = UserRegistrationForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('users:login'))
#     else:
#         form = UserRegistrationForm()
#     context = {'form': form}
#     return render(request, 'users/registrations.html', context)

def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            if 'image' in request.FILES:
                user.image = request.FILES['image']
            user.save()
            return HttpResponseRedirect(reverse('users:login'))
        else:
            print(form.errors) 
    else:
        form = UserRegistrationForm()
    
    context = {'form': form}
    return render(request, 'users/registrations.html', context)




def article_detail(request, article_id):
    article = Article.objects.get(id=article_id)
    context = {'article': article}
    return render(request, 'articles/aboutContent.html', context)    






def training_signup(request):
    if request.method == 'POST':
        form = TrainingForm(request.POST)
        if form.is_valid():
            training_type = form.cleaned_data['training_type']
            day_of_week = form.cleaned_data['day_of_week']
            time = form.cleaned_data['time']
            # Сохранение информации о тренировке в базе данных
            user = request.user
            record = TrainingRecord(user=user, training_type=training_type, day_of_week=day_of_week, time=time)
            record.save()
            
            return redirect('users:training_confirmation')  # Перенаправление на страницу подтверждения
    else:
        form = TrainingForm()
    
    return render(request, 'users/training_signup.html', {'form': form})
def training_confirmation(request):
    # Получение информации о записи пользователя из базы данных
    user = request.user
    training_record = TrainingRecord.objects.filter(user=user).order_by('-id').first()    
    context = {
        'training_record': training_record,
    }
    return render(request, 'users/training_confirmation.html', context)