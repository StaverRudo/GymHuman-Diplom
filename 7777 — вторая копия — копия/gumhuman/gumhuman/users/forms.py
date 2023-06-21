from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from users.models import User
from articles.models import *
from django.contrib.auth import get_user_model


User = get_user_model()

class UserLoginForm(AuthenticationForm):

    username = forms.CharField(widget=forms.TextInput(attrs={

        'class': 'loginblock-left__input', 'placeholder': 'Введите имя пользователя'

    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={

        'class': 'loginblock-right__input', 'placeholder': 'Введите пароль'

    }))

    class Meta:
        model = User
        fields = ('username', 'password')

 
# class UserRegistrationForm(UserCreationForm):
#     first_name = forms.CharField(widget=forms.TextInput(attrs={
#         'class': 'registerblock-left__input', 'placeholder': 'Введите имя пользователя'
#     }))
#     last_name = forms.CharField(widget=forms.TextInput(attrs={
#         'class': 'registerblock-right__input', 'placeholder': 'Введите фамилию пользователя'
#     }))
#     username = forms.CharField(widget=forms.TextInput(attrs={
#         'class': 'registerblock-right__input', 'placeholder': 'Введите username'
#     }))
#     email = forms.EmailField(widget=forms.TextInput(attrs={
#         'class': 'registerblock-right__input', 'placeholder': 'Введите email'
#     }))
#     password1 = forms.CharField(widget=forms.PasswordInput(attrs={
#         'class': 'registerblock-right__input', 'placeholder': 'Введите пароль'
#     }))
#     password2 = forms.CharField(widget=forms.PasswordInput(attrs={
#         'class': 'registerblock-right__input', 'placeholder': 'Повторите пароль'
#     }))
#     image = forms.ImageField(label='Изображение профиля', required=False)

#     class Meta:
#         model = User
#         fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2','image')

#     def save(self, commit=True):
#         user = super().save(commit=False)
#         user.image = self.cleaned_data['image']  # Сохраните загруженное изображение в поле 'image'
#         if commit:
#             user.save()
#         return user    

class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'registerblock-right__input', 'placeholder': 'Введите имя пользователя'
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'registerblock-right__input', 'placeholder': 'Введите фамилию пользователя'
    }))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'registerblock-right__input', 'placeholder': 'Введите username'
    }))
    email = forms.EmailField(widget=forms.TextInput(attrs={
        'class': 'registerblock-right__input', 'placeholder': 'Введите email'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'registerblock-right__input', 'placeholder': 'Введите пароль'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'registerblock-right__input', 'placeholder': 'Повторите пароль'
    }))
    about_me = forms.CharField(widget=forms.Textarea(attrs={
         'class': 'registerblock-right__input_info',
         'placeholder': 'Расскажите о себе',
         'rows': 4, 'cols': 40
    }))
    target = forms.CharField(widget=forms.TextInput(attrs={
         'class': 'registerblock-right__input', 'placeholder': 'Напишите свою главную цель'
    }))
    image = forms.ImageField(label='Изображение профиля', required=False, widget=forms.ClearableFileInput(attrs={'class': 'your-css-class'}))
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2', 'image', 'about_me', 'target')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.image = self.cleaned_data['image']
        if commit:
            user.save()
        return user




class TrainingForm(forms.Form):
    TRAINING_CHOICES = [
        ('Кардио тренировка', 'кардио тренировка'),
        ('Йога', 'йога'),
        ('Бокс', 'бокс'),
        ('Сайкл', 'сайкл'),
        ('Карате', 'карате'),
        ('Кроссфит', 'кроссфит'),
        ('Пилатес', 'пилатес'),
        ('Самбо', 'самбо'),
        ('Воркаут', 'воркаут'),
        ('Бодибилдинг', 'бодибилдинг'),
        ('Танцы', 'танцы'),
        ('Тхэквондо', 'тхэквондо'),
        ('Цигун', 'цигун'),
        ('Зумба', 'зумба'),
        ('Аквааэробика', 'аквааэробика'),
        ('Аэробика', 'Аэробика'),
    ]
    DAY_CHOICES = [
        ('Понедельник', 'Понедельник'),
        ('Вторник', 'Вторник'),
        ('Среда', 'Среда'),
        ('Четверг', 'Четверг'),
        ('Пятница', 'Пятница'),
        ('Суббота', 'Суббота'),
        ('Воскресенье', 'Воскресенье'),
    ]
    
    training_type = forms.ChoiceField(label='Тип тренировки', choices=TRAINING_CHOICES)
    day_of_week = forms.ChoiceField(label='День недели', choices=DAY_CHOICES)
    time = forms.TimeField(label='Время', widget=forms.TimeInput(attrs={'placeholder': 'HH:MM'}))


