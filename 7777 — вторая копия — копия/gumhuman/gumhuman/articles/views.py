from django.shortcuts import render, get_object_or_404, redirect
from articles.models import *
from .forms import CommentForm, ContactForm
from articles.models import Comment
from django.core.paginator import Paginator
from django.core.mail import send_mail
import asyncio
from telegram import Bot  # Добавлен импорт класса Bot
from telegram.error import TelegramError
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Message

# Create your views here.
def index(request):
    context = {
         'home': Home.objects.first(),
    }
    return render(request, 'articles/index.html',context)








async def send_telegram_message(chat_id, message):
    bot = Bot(token=settings.TELEGRAM_BOT_TOKEN)
    try:
        await bot.send_message(chat_id=chat_id, text=message)
    except TelegramError as e:
        print(f"An error occurred while sending the message to Telegram: {str(e)}")

# Ваш остальной код...

def about(request):
    articles = Article.objects.all()
    paginator = Paginator(articles, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    categories = ArticleCategory.objects.all()
    arhiv = ArhivCategory.objects.all()
    latest_comments = Comment.objects.order_by('-id')[:3]

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')


        # Отправка сообщения в Telegram
        chat_id = '657099124'  # Замените на ваш chat_id
        telegram_message = f'Имя: {name}\nEmail: {email}\nЗаголовок: {subject}\nСообщение: {message}'
        asyncio.run(send_telegram_message(chat_id, telegram_message))
       

    context = {
        'page_obj': page_obj,
        'categories': categories,
        'arhiv': arhiv,
        'latest_comments': latest_comments,
        'about': About.objects.first(),
    }
    return render(request, 'articles/about.html', context)


def article_search(request):
    query = request.GET.get('q')
    articles = Article.objects.filter(name__icontains=query)
    context = {
        'query': query,
        'articles': articles,
        'categories': ArticleCategory.objects.all(),
        'arhiv': ArhivCategory.objects.all(),
        'latest_comments': Comment.objects.order_by('-id')[:3],
    }
    return render(request, 'articles/article_search.html', context)


def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    comments = Comment.objects.filter(article=article)
    comment_count = comments.count() 

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.article = article
            comment.save()
            return redirect('articles:article_detail', article_id=article.id)
    else:
        form = CommentForm()

    context = {
        'article': article,
        'comments': comments,
        'form': form,
        'comment_count': comment_count,
        'latest_comments': Comment.objects.order_by('-id')[:3],
        'arhiv': ArhivCategory.objects.all(),
        'categories': ArticleCategory.objects.all(),
       
    }
    return render(request, 'articles/aboutContent.html', context)



def todo(request):
    return render(request, 'articles/todo.html')

def calories(request):
    return render(request, 'articles/calories.html')




    
def video(request):
    
    return render(request, 'articles/video.html')

def hand(request):
    return render(request, 'articles/ruki.html')
def shoulders(request):
    return render(request, 'articles/plechi.html')
def back(request):
    return render(request, 'articles/spina.html')
def foot(request):
    return render(request, 'articles/nogi.html')
def chest(request):
    return render(request, 'articles/grud.html')

def raspisanie(request):
    return render(request, 'articles/raspisanie.html')

def prace(request):
    return render(request, 'articles/prace.html')


def error_404(request, exception):
    return render(request, 'articles/404.html', status=404)




def article_filter(request):
    category_id = request.GET.get('category')
    arhiv_id = request.GET.get('arhiv')
    articles = Article.objects.all()

    if category_id:
        category = get_object_or_404(ArticleCategory, id=category_id)
        articles = articles.filter(category=category)

    if arhiv_id:
        arhiv = get_object_or_404(ArhivCategory, id=arhiv_id)
        articles = articles.filter(arhiv=arhiv)

    context = {
        'articles': articles,
        'categories': ArticleCategory.objects.all(),
        'arhivs': ArhivCategory.objects.all(),
    }
    return render(request, 'articles/aboutFilterCategory.html', context)


def article_filterr(request):
    category_id = request.GET.get('category')
    arhiv_id = request.GET.get('arhiv')
    articles = Article.objects.all()

    if category_id:
        category = get_object_or_404(ArticleCategory, id=category_id)
        articles = articles.filter(category=category)

    if arhiv_id:
        arhiv = get_object_or_404(ArhivCategory, id=arhiv_id)
        articles = articles.filter(arhiv=arhiv)

    context = {
        'articles': articles,
        'categories': ArticleCategory.objects.all(),
        'arhivs': ArhivCategory.objects.all(),
    }
    return render(request, 'articles/aboutFilterArhiv.html', context)




# ----------------------------------------------------------------------------------------------

from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required
def feedback(request):
    if request.method == 'POST':
        recipient_id = request.POST['recipient_id']
        text = request.POST['text']
        sender = request.user
        recipient = User.objects.get(id=recipient_id)
        
        is_from_admin = sender.is_staff  # Проверка, что отправитель является администратором
        message = Message.objects.create(sender=sender, recipient=recipient, text=text, is_from_admin=is_from_admin)
        messages.success(request, 'Сообщение успешно отправлено.')
        return redirect('articles:feedback')
    
    users = User.objects.exclude(id=request.user.id)
    return render(request, 'articles/feedback.html', {'users': users})




def inbox(request):
    messages = Message.objects.filter(recipient=request.user)
    return render(request, 'articles/inbox.html', {'messages': messages})




def reply(request, message_id):
    original_message = Message.objects.get(id=message_id)
    reply_text = request.POST['reply_text']
    
    sender = request.user
    recipient = original_message.sender
    
    reply_message = Message.objects.create(sender=sender, recipient=recipient, text=reply_text)
    messages.success(request, 'Ответ успешно отправлен.')
    
    return redirect('articles:inbox')

