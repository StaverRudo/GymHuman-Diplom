from django.db import models
from django.contrib.auth import get_user_model
from users.models import *

# Create your models here.

# Категории
class ArticleCategory(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Категория статей'
        verbose_name_plural = 'Категории статей'    

# Архив статей по месяцам
class ArhivCategory(models.Model):
    name = models.CharField(max_length=128,null=True)
    description = models.TextField(null=True)
                                   
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Архив по месяцам'
        verbose_name_plural = 'Архив по месяцам'
# Статьи
class Article(models.Model):
    name = models.CharField(max_length=256, unique=True)    
    description = models.TextField()
    date = models.DateTimeField()
    title = models.CharField(max_length=128,null=True)
    info = models.TextField(null=True)
    image_one = models.ImageField(upload_to='articles_images', default='cris2.jpg')  
    image_two = models.ImageField(upload_to='articles_images', default='cris2.jpg')  
    title_mini = models.CharField(max_length=128,null=True)
    info_mini = models.TextField(null=True)
    user = models.CharField(max_length=47)
    image = models.ImageField(upload_to='articles_images', default='cris2.jpg', blank=True, null=True)    
# Связь с категорией
    category = models.ForeignKey(to=ArticleCategory, on_delete=models.CASCADE)
# Связь с архивом    
    arhiv = models.ForeignKey(to=ArhivCategory, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return f'Статья {self.name} | Категория {self.category.name}'
    class Meta:
        verbose_name = 'Статьи'
        verbose_name_plural = 'Статьи'






# Создаю модель для главной страницы, чтобы была возможность изменять данные        

class Home(models.Model):
    title = models.CharField(max_length=256, unique=True, verbose_name='Заголовок сайта')  
    title_image = models.ImageField(upload_to='articles_images', verbose_name='Изображение зоголовка сайта') 
    logo_image = models.ImageField(upload_to='articles_images', verbose_name='Изображение логотипа') 
    title_logo_one = models.CharField(max_length=126, unique=True, verbose_name='Текст первой части логотипа') 
    title_logo_two = models.CharField(max_length=126, unique=True, verbose_name='Текст второй части логотипа') 
    login_text_one = models.CharField(max_length=256, unique=True, verbose_name='Первая кнопка входа')  
    login_text_two = models.CharField(max_length=256, unique=True, verbose_name='Вторая кнопка входа')  
    strelka_image = models.ImageField(upload_to='articles_images', verbose_name='Изображение для возврата в начало сайта')
    slider_text_one = models.CharField(max_length=256, unique=True, verbose_name='Первый текст на слайдере')
    slider_button_one = models.CharField(max_length=256, unique=True, verbose_name='Первая кнопка на слайдере')
    slider_image_one = models.ImageField(upload_to='articles_images', verbose_name='Первое изображение слайдера') 
    slider_text_two = models.CharField(max_length=256, unique=True, verbose_name='Второй текст на слайдере')
    slider_button_two = models.CharField(max_length=256, unique=True, verbose_name='Второе изображение слайдера')
    slider_image_two = models.ImageField(upload_to='articles_images', verbose_name='Второе изображение слайдера') 
    info_title = models.CharField(max_length=256, unique=True, verbose_name='Заголовок блока info')
    info_description = models.TextField(verbose_name='Описание к блоку info')
    infoblock_card_image_one = models.ImageField(upload_to='articles_images', verbose_name='Первое изображение блока info')
    infoblock_card_title_one = models.CharField(max_length=256, unique=True, verbose_name='Первый заголовок блока info')
    infoblock_card_description_one = models.TextField(verbose_name='Первое описание блока info')
    infoblock_card_image_two = models.ImageField(upload_to='articles_images', verbose_name='Второе изображение блока info')
    infoblock_card_title_two = models.CharField(max_length=126, unique=True, verbose_name='Второй заголовок блока info')
    infoblock_card_description_two = models.TextField(verbose_name='Второе описание блока info')
    infoblock_card_image_three = models.ImageField(upload_to='articles_images', verbose_name='Третье изображение блока info')
    infoblock_card_title_three = models.CharField(max_length=126, unique=True, verbose_name='Третий заголовок блока info')
    infoblock_card_description_three = models.TextField(verbose_name='Третье описание блока info')
    tools_title = models.CharField(max_length=256, unique=True, verbose_name='Заголовок блока tools')
    tools_text = models.TextField(verbose_name='Описание блока tools')
    tools_item_image_one = models.ImageField(upload_to='articles_images', verbose_name='Первое изображение карточки блока tools')
    tools_item_title_one = models.CharField(max_length=256, unique=True, verbose_name='Первый заголовок карточки блока tools')
    tools_item_text_one = models.TextField(verbose_name='Описание первой карточки блока tools')
    tools_item_image_two = models.ImageField(upload_to='articles_images', verbose_name='Второе изображение карточки блока tools')
    tools_item_title_two = models.CharField(max_length=256, unique=True, verbose_name='Второй заголовок карточки блока tools')
    tools_item_text_two = models.TextField(verbose_name='Описание второй карточки блока tools')
    tools_item_image_three = models.ImageField(upload_to='articles_images', verbose_name='Третье изображение карточки блока tools')
    tools_item_title_three = models.CharField(max_length=256, unique=True, verbose_name='Третий заголовок карточки блока tools')
    tools_item_text_three = models.TextField(verbose_name='Описание третей карточки блока tools')
    footer_title = models.CharField(max_length=256, unique=True, verbose_name='Заголовок блока footer')
    class Meta:
        verbose_name = 'Главная страница'
        verbose_name_plural = 'Главная страница'




# ...

from .telegram_utils import send_telegram_message

class Comment(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    article = models.ForeignKey('Article', on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Комментарий {self.pk} от {self.user.username}'

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

 



# Эбаут создаю модель которая будет отвечать за страницу articles, за то что на ней отображено         
class About(models.Model):
    title_about = models.CharField(max_length=256, unique=True, verbose_name='Заголовок about') 
    title_image = models.ImageField(upload_to='articles_images', verbose_name='Изображение title') 
    logo_image = models.ImageField(upload_to='articles_images', verbose_name='Изображение логотипа') 
    header_logo_one = models.CharField(max_length=126, unique=True, verbose_name='Текст первой части логотипа') 
    header_logo_two = models.CharField(max_length=126, unique=True, verbose_name='Текст второй части логотипа')
    about_title = models.CharField(max_length=126, unique=True, verbose_name='Текст первой вкладки меню')
    about_title_two = models.CharField(max_length=126, unique=True, verbose_name='Текст второй вкладки меню')
    about_title_three = models.CharField(max_length=126, unique=True, verbose_name='Текст третей вкладки меню')
    burger_title = models.CharField(max_length=126, unique=True, verbose_name='Текст в бургер  меню')
    about_images = models.CharField(max_length=126, unique=True, verbose_name='Главный текст в about_images')
    about_images_title = models.CharField(max_length=126, unique=True, verbose_name='Втрой текст в about_images')
    about_images_text = models.CharField(max_length=126, unique=True, verbose_name='Третий текст в about_images')
    profile_more_text = models.CharField(max_length=126, unique=True, verbose_name='Первый текст в профиле')
    profile_more_text_two = models.CharField(max_length=126, unique=True, verbose_name='Второй текст в профиле', default='О себе:')
    strelka_image = models.ImageField(upload_to='articles_images', verbose_name='Изображение для возврата в начало сайта')
    sidebar_input = models.CharField(max_length=126, unique=True, verbose_name='Текст в placeholder поиска')
    sidebar_button = models.CharField(max_length=126, unique=True, verbose_name='Текст кнопки поиска')
    sidebar_title = models.CharField(max_length=126, unique=True, verbose_name='Заголовок категорий')
    sidebar_arhive_titile = models.CharField(max_length=126, unique=True, verbose_name='Заголовок архива')
    sidebar_comments_title = models.CharField(max_length=126, unique=True, verbose_name='Заголовок последних комментариев')
    content_buttonblock_button = models.CharField(max_length=126, unique=True, verbose_name='Текст кнопки показа следующий статей')
    modal_title = models.CharField(max_length=126, unique=True, verbose_name='Заголовок формы')
    modal_form_top_tile_one = models.CharField(max_length=126, unique=True, verbose_name='Первое поле input формы')
    modal_form_top_tile_two = models.CharField(max_length=126, unique=True, verbose_name='Второе поле input формы')
    modal_form_top_tile_three = models.CharField(max_length=126, unique=True, verbose_name='Третье поле input формы')
    modal_form_top_tile_fo = models.CharField(max_length=126, unique=True, verbose_name='Четвертое поле input формы')
    modal_form_top_tile_five = models.CharField(max_length=126, unique=True, verbose_name='Пятое поле input формы')
    index_btn = models.CharField(max_length=126, unique=True, verbose_name='Текст кнопки формы')
    button_look = models.ImageField(upload_to='articles_images', verbose_name='Изображение бокового меню')
    right_bar_images_one = models.ImageField(upload_to='articles_images', verbose_name='Первое изображение бокового меню')
    right_bar_images_two = models.ImageField(upload_to='articles_images', verbose_name='Второе изображение бокового меню')
    right_bar_images_three = models.ImageField(upload_to='articles_images', verbose_name='Третье изображение бокового меню')
    right_bar_images_fo = models.ImageField(upload_to='articles_images', verbose_name='Четвертое изображение бокового меню')


    def __str__(self):
        return self.title_about

    class Meta:
        verbose_name = 'Страница About'
        verbose_name_plural = 'Страница About'




# ---------------------------------------------------------------------------------------------------------
class One(models.Model):
    title_about = models.CharField(max_length=256, unique=True, verbose_name='Заголовок about') 
    title_image = models.ImageField(upload_to='articles_images', verbose_name='Изображение title') 
    logo_image = models.ImageField(upload_to='articles_images', verbose_name='Изображение логотипа') 
    header_logo_one = models.CharField(max_length=126, unique=True, verbose_name='Текст первой части логотипа') 
    header_logo_two = models.CharField(max_length=126, unique=True, verbose_name='Текст второй части логотипа')
    about_title = models.CharField(max_length=126, unique=True, verbose_name='Текст первой вкладки меню')
    about_title_two = models.CharField(max_length=126, unique=True, verbose_name='Текст второй вкладки меню')
    about_title_three = models.CharField(max_length=126, unique=True, verbose_name='Текст третей вкладки меню')
    burger_title = models.CharField(max_length=126, unique=True, verbose_name='Текст в бургер  меню')
    about_images = models.CharField(max_length=126, unique=True, verbose_name='Главный текст в about_images')
    about_images_title = models.CharField(max_length=126, unique=True, verbose_name='Втрой текст в about_images')
    about_images_text = models.CharField(max_length=126, unique=True, verbose_name='Третий текст в about_images')
    # ---------------------------------------------------------------------------------------------------------------------
    one_title = models.CharField(max_length=256, unique=True, verbose_name='Заголовок категорий') 
    # ----------------------------------------------------------------------------------------------------------------------
    one_title_one = models.CharField(max_length=256, unique=True, verbose_name='Текст первой категории') 
    one_title_two = models.CharField(max_length=256, unique=True, verbose_name='Текст второй категории') 
    one_title_three = models.CharField(max_length=256, unique=True, verbose_name='Текст третий категории') 
    one_title_fo = models.CharField(max_length=256, unique=True, verbose_name='Текст четвертой категории') 
    one_title_five = models.CharField(max_length=256, unique=True, verbose_name='Текст пятой категории') 
    one_title_six = models.CharField(max_length=256, unique=True, verbose_name='Текст шестой категории') 
    # ----------------------------------------------------------------------------------------------------------------------

    one_content_title = models.CharField(max_length=256, unique=True, verbose_name='Заголовок контекста первый') 
    one_content_text = models.TextField(max_length=456, unique=True, verbose_name='Текст первый контекста') 
    one_content_title_two = models.CharField(max_length=256, unique=True, verbose_name='Заголовок контекста второй') 
    one_content_text_two = models.TextField(max_length=456, unique=True, verbose_name='Текст второй контекста') 
    one_content_title_three = models.CharField(max_length=256, unique=True, verbose_name='Заголовок контекста третий') 
    one_content_text_three = models.TextField(max_length=456, unique=True, verbose_name='Текст третий контекста') 
    one_content_title_fo = models.CharField(max_length=256, unique=True, verbose_name='Заголовок контекста четвертый')
    # --------------------------------------------------------------------------------------------------------------------------
    one_button = models.CharField(max_length=256, unique=True, verbose_name='Текст первой кнопки')
    one_button_two = models.CharField(max_length=256, unique=True, verbose_name='Текст второй кнопки')
    # --------------------------------------------------------------------------------------------------------------------------
    one_modal_title = models.CharField(max_length=256, unique=True, verbose_name='Заголовок модального окна')
    one_image_one = models.ImageField(upload_to='articles_images', verbose_name='Первое изображение модального окна') 
    one_image_two = models.ImageField(upload_to='articles_images', verbose_name='Второе изображение модального окна') 
    one_image_three = models.ImageField(upload_to='articles_images', verbose_name='Третье изображение модального окна') 
    one_image_fo = models.ImageField(upload_to='articles_images', verbose_name='Четвертое изображение модального окна') 
    one_modal_title_min = models.CharField(max_length=256, unique=True, verbose_name='Второй заголовок модального окна')
    one_modal_description = models.CharField(max_length=256, unique=True, verbose_name='Второое описание модального окна')


    one_modal_title_t = models.CharField(max_length=256, unique=True, verbose_name='Заголовок модального окна')
    one_image_one_t = models.ImageField(upload_to='articles_images', verbose_name='Первое изображение модального окна') 
    one_modal_title_min_t = models.CharField(max_length=256, unique=True, verbose_name='Второй заголовок модального окна')
    one_modal_description_t = models.CharField(max_length=256, unique=True, verbose_name='Второое описание модального окна')






    
    def __str__(self):
        return self.title_about

    class Meta:
        verbose_name = 'Первая страница упражнений'
        verbose_name_plural = 'Первая страница упражнений'




# ---------------------------------------------------------------------------------------------------------
class Two(models.Model):
    title_about = models.CharField(max_length=256, unique=True, verbose_name='Заголовок about') 
    title_image = models.ImageField(upload_to='articles_images', verbose_name='Изображение title') 
    logo_image = models.ImageField(upload_to='articles_images', verbose_name='Изображение логотипа') 
    header_logo_one = models.CharField(max_length=126, unique=True, verbose_name='Текст первой части логотипа') 
    header_logo_two = models.CharField(max_length=126, unique=True, verbose_name='Текст второй части логотипа')
    about_title = models.CharField(max_length=126, unique=True, verbose_name='Текст первой вкладки меню')
    about_title_two = models.CharField(max_length=126, unique=True, verbose_name='Текст второй вкладки меню')
    about_title_three = models.CharField(max_length=126, unique=True, verbose_name='Текст третей вкладки меню')
    burger_title = models.CharField(max_length=126, unique=True, verbose_name='Текст в бургер  меню')
    about_images = models.CharField(max_length=126, unique=True, verbose_name='Главный текст в about_images')
    about_images_title = models.CharField(max_length=126, unique=True, verbose_name='Втрой текст в about_images')
    about_images_text = models.CharField(max_length=126, unique=True, verbose_name='Третий текст в about_images')
    # ---------------------------------------------------------------------------------------------------------------------
    two_title = models.CharField(max_length=256, unique=True, verbose_name='Заголовок категорий') 
    # ----------------------------------------------------------------------------------------------------------------------
    two_title_one = models.CharField(max_length=256, unique=True, verbose_name='Текст первой категории') 
    two_title_two = models.CharField(max_length=256, unique=True, verbose_name='Текст второй категории') 
    two_title_three = models.CharField(max_length=256, unique=True, verbose_name='Текст третий категории') 
    two_title_fo = models.CharField(max_length=256, unique=True, verbose_name='Текст четвертой категории') 
    two_title_five = models.CharField(max_length=256, unique=True, verbose_name='Текст пятой категории') 
    two_title_six = models.CharField(max_length=256, unique=True, verbose_name='Текст шестой категории') 
    # ----------------------------------------------------------------------------------------------------------------------

    two_content_title = models.CharField(max_length=256, unique=True, verbose_name='Заголовок контекста первый') 
    two_content_text = models.TextField(max_length=456, unique=True, verbose_name='Текст первый контекста') 
    two_content_title_two = models.CharField(max_length=256, unique=True, verbose_name='Заголовок контекста второй') 
    two_content_text_two = models.TextField(max_length=456, unique=True, verbose_name='Текст второй контекста') 
    two_content_title_three = models.CharField(max_length=256, unique=True, verbose_name='Заголовок контекста третий') 
    two_content_text_three = models.TextField(max_length=456, unique=True, verbose_name='Текст третий контекста') 
    two_content_title_fo = models.CharField(max_length=256, unique=True, verbose_name='Заголовок контекста четвертый')
    # --------------------------------------------------------------------------------------------------------------------------
    two_button = models.CharField(max_length=256, unique=True, verbose_name='Текст первой кнопки')
    two_button_two = models.CharField(max_length=256, unique=True, verbose_name='Текст второй кнопки')
    # --------------------------------------------------------------------------------------------------------------------------
    two_modal_title = models.CharField(max_length=256, unique=True, verbose_name='Заголовок модального окна')
    two_image_one = models.ImageField(upload_to='articles_images', verbose_name='Первое изображение модального окна') 
    two_image_two = models.ImageField(upload_to='articles_images', verbose_name='Второе изображение модального окна') 
    two_modal_title_min = models.CharField(max_length=256, unique=True, verbose_name='Второй заголовок модального окна')
    two_modal_description = models.CharField(max_length=256, unique=True, verbose_name='Второое описание модального окна')

    two_modal_title_t = models.CharField(max_length=256, unique=True, verbose_name='Заголовок модального окна')
    two_image_one_t = models.ImageField(upload_to='articles_images', verbose_name='Первое изображение модального окна') 
    two_image_two_t = models.ImageField(upload_to='articles_images', verbose_name='Второе изображение модального окна') 
    two_modal_title_min_t = models.CharField(max_length=256, unique=True, verbose_name='Второй заголовок модального окна')
    two_modal_description_t = models.CharField(max_length=256, unique=True, verbose_name='Второое описание модального окна')

    two_modal_title_r = models.CharField(max_length=256, unique=True, verbose_name='Заголовок модального окна')
    two_image_one_r = models.ImageField(upload_to='articles_images', verbose_name='Первое изображение модального окна') 
    two_image_two_r = models.ImageField(upload_to='articles_images', verbose_name='Второе изображение модального окна') 
    two_modal_title_min_r = models.CharField(max_length=256, unique=True, verbose_name='Второй заголовок модального окна')
    two_modal_description_r = models.CharField(max_length=256, unique=True, verbose_name='Второое описание модального окна')

    two_modal_title_e = models.CharField(max_length=256, unique=True, verbose_name='Заголовок модального окна')
    two_image_one_e = models.ImageField(upload_to='articles_images', verbose_name='Первое изображение модального окна') 
    two_image_two_e = models.ImageField(upload_to='articles_images', verbose_name='Второе изображение модального окна') 
    two_modal_title_min_e = models.CharField(max_length=256, unique=True, verbose_name='Второй заголовок модального окна')
    two_modal_description_e = models.CharField(max_length=256, unique=True, verbose_name='Второое описание модального окна')

    def __str__(self):
        return self.title_about

    class Meta:
        verbose_name = 'Вторая страница упражнений'
        verbose_name_plural = 'Вторая страница упражнений'      




# ---------------------------------------------------------------------------------------------------------
class Three(models.Model):
    title_about = models.CharField(max_length=256, unique=True, verbose_name='Заголовок about') 
    title_image = models.ImageField(upload_to='articles_images', verbose_name='Изображение title') 
    logo_image = models.ImageField(upload_to='articles_images', verbose_name='Изображение логотипа') 
    header_logo_one = models.CharField(max_length=126, unique=True, verbose_name='Текст первой части логотипа') 
    header_logo_two = models.CharField(max_length=126, unique=True, verbose_name='Текст второй части логотипа')
    about_title = models.CharField(max_length=126, unique=True, verbose_name='Текст первой вкладки меню')
    about_title_two = models.CharField(max_length=126, unique=True, verbose_name='Текст второй вкладки меню')
    about_title_three = models.CharField(max_length=126, unique=True, verbose_name='Текст третей вкладки меню')
    burger_title = models.CharField(max_length=126, unique=True, verbose_name='Текст в бургер  меню')
    about_images = models.CharField(max_length=126, unique=True, verbose_name='Главный текст в about_images')
    about_images_title = models.CharField(max_length=126, unique=True, verbose_name='Втрой текст в about_images')
    about_images_text = models.CharField(max_length=126, unique=True, verbose_name='Третий текст в about_images')
    # ---------------------------------------------------------------------------------------------------------------------
    three_title = models.CharField(max_length=256, unique=True, verbose_name='Заголовок категорий') 
    # ----------------------------------------------------------------------------------------------------------------------
    three_title_one = models.CharField(max_length=256, unique=True, verbose_name='Текст первой категории') 
    three_title_two = models.CharField(max_length=256, unique=True, verbose_name='Текст второй категории') 
    three_title_three = models.CharField(max_length=256, unique=True, verbose_name='Текст третий категории') 
    three_title_fo = models.CharField(max_length=256, unique=True, verbose_name='Текст четвертой категории') 
    three_title_five = models.CharField(max_length=256, unique=True, verbose_name='Текст пятой категории') 
    three_title_six = models.CharField(max_length=256, unique=True, verbose_name='Текст шестой категории') 
    # ----------------------------------------------------------------------------------------------------------------------

    three_content_title = models.CharField(max_length=256, unique=True, verbose_name='Заголовок контекста первый') 
    three_content_text = models.TextField(max_length=456, unique=True, verbose_name='Текст первый контекста') 
    three_content_title_two = models.CharField(max_length=256, unique=True, verbose_name='Заголовок контекста второй') 
    three_content_text_two = models.TextField(max_length=456, unique=True, verbose_name='Текст второй контекста') 
    three_content_title_three = models.CharField(max_length=256, unique=True, verbose_name='Заголовок контекста третий') 
    three_content_text_three = models.TextField(max_length=456, unique=True, verbose_name='Текст третий контекста') 
    three_content_title_fo = models.CharField(max_length=256, unique=True, verbose_name='Заголовок контекста четвертый')
    # --------------------------------------------------------------------------------------------------------------------------
    three_button = models.CharField(max_length=256, unique=True, verbose_name='Текст первой кнопки')
    three_button_two = models.CharField(max_length=256, unique=True, verbose_name='Текст второй кнопки')
    # --------------------------------------------------------------------------------------------------------------------------
    three_modal_title = models.CharField(max_length=256, unique=True, verbose_name='Заголовок модального окна')
    three_image_one = models.ImageField(upload_to='articles_images', verbose_name='Первое изображение модального окна') 
    three_image_two = models.ImageField(upload_to='articles_images', verbose_name='Второе изображение модального окна') 
    three_modal_title_min = models.CharField(max_length=256, unique=True, verbose_name='Второй заголовок модального окна')
    three_modal_description = models.CharField(max_length=256, unique=True, verbose_name='Второое описание модального окна')

    three_modal_title_t = models.CharField(max_length=256, unique=True, verbose_name='Заголовок модального окна')
    three_image_one_t = models.ImageField(upload_to='articles_images', verbose_name='Первое изображение модального окна') 
    three_image_two_t = models.ImageField(upload_to='articles_images', verbose_name='Второе изображение модального окна') 
    three_modal_title_min_t = models.CharField(max_length=256, unique=True, verbose_name='Второй заголовок модального окна')
    three_modal_description_t = models.CharField(max_length=256, unique=True, verbose_name='Второое описание модального окна')

    three_modal_title_r = models.CharField(max_length=256, unique=True, verbose_name='Заголовок модального окна')
    three_image_one_r = models.ImageField(upload_to='articles_images', verbose_name='Первое изображение модального окна') 
    three_image_two_r = models.ImageField(upload_to='articles_images', verbose_name='Второе изображение модального окна') 
    three_modal_title_min_r = models.CharField(max_length=256, unique=True, verbose_name='Второй заголовок модального окна')
    three_modal_description_r = models.CharField(max_length=256, unique=True, verbose_name='Второое описание модального окна')

    three_modal_title_e = models.CharField(max_length=256, unique=True, verbose_name='Заголовок модального окна')
    three_image_one_e = models.ImageField(upload_to='articles_images', verbose_name='Первое изображение модального окна') 
    three_image_two_e = models.ImageField(upload_to='articles_images', verbose_name='Второе изображение модального окна') 
    three_modal_title_min_e = models.CharField(max_length=256, unique=True, verbose_name='Второй заголовок модального окна')
    three_modal_description_e = models.CharField(max_length=256, unique=True, verbose_name='Второое описание модального окна')

    def __str__(self):
        return self.title_about

    class Meta:
        verbose_name = 'Третья страница упражнений'
        verbose_name_plural = 'третья страница упражнений'                






# ---------------------------------------------------------------------------------------------------------
class Fo(models.Model):
    title_about = models.CharField(max_length=256, unique=True, verbose_name='Заголовок about') 
    title_image = models.ImageField(upload_to='articles_images', verbose_name='Изображение title') 
    logo_image = models.ImageField(upload_to='articles_images', verbose_name='Изображение логотипа') 
    header_logo_one = models.CharField(max_length=126, unique=True, verbose_name='Текст первой части логотипа') 
    header_logo_two = models.CharField(max_length=126, unique=True, verbose_name='Текст второй части логотипа')
    about_title = models.CharField(max_length=126, unique=True, verbose_name='Текст первой вкладки меню')
    about_title_two = models.CharField(max_length=126, unique=True, verbose_name='Текст второй вкладки меню')
    about_title_three = models.CharField(max_length=126, unique=True, verbose_name='Текст третей вкладки меню')
    burger_title = models.CharField(max_length=126, unique=True, verbose_name='Текст в бургер  меню')
    about_images = models.CharField(max_length=126, unique=True, verbose_name='Главный текст в about_images')
    about_images_title = models.CharField(max_length=126, unique=True, verbose_name='Втрой текст в about_images')
    about_images_text = models.CharField(max_length=126, unique=True, verbose_name='Третий текст в about_images')
    # ---------------------------------------------------------------------------------------------------------------------
    fo_title = models.CharField(max_length=256, unique=True, verbose_name='Заголовок категорий') 
    # ----------------------------------------------------------------------------------------------------------------------
    fo_title_one = models.CharField(max_length=256, unique=True, verbose_name='Текст первой категории') 
    fo_title_two = models.CharField(max_length=256, unique=True, verbose_name='Текст второй категории') 
    fo_title_three = models.CharField(max_length=256, unique=True, verbose_name='Текст третий категории') 
    fo_title_fo = models.CharField(max_length=256, unique=True, verbose_name='Текст четвертой категории') 
    fo_title_five = models.CharField(max_length=256, unique=True, verbose_name='Текст пятой категории') 
    fo_title_six = models.CharField(max_length=256, unique=True, verbose_name='Текст шестой категории') 
    # ----------------------------------------------------------------------------------------------------------------------

    fo_content_title = models.CharField(max_length=256, unique=True, verbose_name='Заголовок контекста первый') 
    fo_content_text = models.TextField(max_length=456, unique=True, verbose_name='Текст первый контекста') 
    fo_content_title_two = models.CharField(max_length=256, unique=True, verbose_name='Заголовок контекста второй') 
    fo_content_text_two = models.TextField(max_length=456, unique=True, verbose_name='Текст второй контекста') 
    fo_content_title_three = models.CharField(max_length=256, unique=True, verbose_name='Заголовок контекста третий') 
    fo_content_text_three = models.TextField(max_length=456, unique=True, verbose_name='Текст третий контекста') 
    fo_content_title_fo = models.CharField(max_length=256, unique=True, verbose_name='Заголовок контекста четвертый')
    # --------------------------------------------------------------------------------------------------------------------------
    fo_button = models.CharField(max_length=256, unique=True, verbose_name='Текст первой кнопки')
    fo_button_two = models.CharField(max_length=256, unique=True, verbose_name='Текст второй кнопки')
    # --------------------------------------------------------------------------------------------------------------------------
    fo_modal_title = models.CharField(max_length=256, unique=True, verbose_name='Заголовок модального окна')
    fo_image_one = models.ImageField(upload_to='articles_images', verbose_name='Первое изображение модального окна') 
    fo_modal_title_min = models.CharField(max_length=256, unique=True, verbose_name='Второй заголовок модального окна')
    fo_modal_description = models.CharField(max_length=256, unique=True, verbose_name='Второое описание модального окна')

    fo_modal_title_t = models.CharField(max_length=256, unique=True, verbose_name='Заголовок модального окна')
    fo_image_one_t = models.ImageField(upload_to='articles_images', verbose_name='Первое изображение модального окна') 
    fo_image_two_t = models.ImageField(upload_to='articles_images', verbose_name='Второе изображение модального окна') 
    fo_modal_title_min_t = models.CharField(max_length=256, unique=True, verbose_name='Второй заголовок модального окна')
    fo_modal_description_t = models.CharField(max_length=256, unique=True, verbose_name='Второое описание модального окна')

    fo_modal_title_r = models.CharField(max_length=256, unique=True, verbose_name='Заголовок модального окна')
    fo_image_one_r = models.ImageField(upload_to='articles_images', verbose_name='Первое изображение модального окна') 
    fo_image_two_r = models.ImageField(upload_to='articles_images', verbose_name='Второе изображение модального окна') 
    fo_modal_title_min_r = models.CharField(max_length=256, unique=True, verbose_name='Второй заголовок модального окна')
    fo_modal_description_r = models.CharField(max_length=256, unique=True, verbose_name='Второое описание модального окна')

    fo_modal_title_e = models.CharField(max_length=256, unique=True, verbose_name='Заголовок модального окна')
    fo_image_one_e = models.ImageField(upload_to='articles_images', verbose_name='Первое изображение модального окна') 
    fo_modal_title_min_e = models.CharField(max_length=256, unique=True, verbose_name='Второй заголовок модального окна')
    fo_modal_description_e = models.CharField(max_length=256, unique=True, verbose_name='Второое описание модального окна')

    def __str__(self):
        return self.title_about

    class Meta:
        verbose_name = 'Четвертая страница упражнений'
        verbose_name_plural = 'Четвертая страница упражнений'     


# ---------------------------------------------------------------------------------------------------------
class Five(models.Model):
    title_about = models.CharField(max_length=256, unique=True, verbose_name='Заголовок about') 
    title_image = models.ImageField(upload_to='articles_images', verbose_name='Изображение title') 
    logo_image = models.ImageField(upload_to='articles_images', verbose_name='Изображение логотипа') 
    header_logo_one = models.CharField(max_length=126, unique=True, verbose_name='Текст первой части логотипа') 
    header_logo_two = models.CharField(max_length=126, unique=True, verbose_name='Текст второй части логотипа')
    about_title = models.CharField(max_length=126, unique=True, verbose_name='Текст первой вкладки меню')
    about_title_two = models.CharField(max_length=126, unique=True, verbose_name='Текст второй вкладки меню')
    about_title_three = models.CharField(max_length=126, unique=True, verbose_name='Текст третей вкладки меню')
    burger_title = models.CharField(max_length=126, unique=True, verbose_name='Текст в бургер  меню')
    about_images = models.CharField(max_length=126, unique=True, verbose_name='Главный текст в about_images')
    about_images_title = models.CharField(max_length=126, unique=True, verbose_name='Втрой текст в about_images')
    about_images_text = models.CharField(max_length=126, unique=True, verbose_name='Третий текст в about_images')
    # ---------------------------------------------------------------------------------------------------------------------
    five_title = models.CharField(max_length=256, unique=True, verbose_name='Заголовок категорий') 
    # ----------------------------------------------------------------------------------------------------------------------
    five_title_one = models.CharField(max_length=256, unique=True, verbose_name='Текст первой категории') 
    five_title_two = models.CharField(max_length=256, unique=True, verbose_name='Текст второй категории') 
    five_title_three = models.CharField(max_length=256, unique=True, verbose_name='Текст третий категории') 
    five_title_fo = models.CharField(max_length=256, unique=True, verbose_name='Текст четвертой категории') 
    five_title_five = models.CharField(max_length=256, unique=True, verbose_name='Текст пятой категории') 
    five_title_six = models.CharField(max_length=256, unique=True, verbose_name='Текст шестой категории') 
    # ----------------------------------------------------------------------------------------------------------------------

    five_content_title = models.CharField(max_length=256, unique=True, verbose_name='Заголовок контекста первый') 
    five_content_text = models.TextField(max_length=456, unique=True, verbose_name='Текст первый контекста') 
    five_content_title_two = models.CharField(max_length=256, unique=True, verbose_name='Заголовок контекста второй') 
    five_content_text_two = models.TextField(max_length=456, unique=True, verbose_name='Текст второй контекста') 
    five_content_title_three = models.CharField(max_length=256, unique=True, verbose_name='Заголовок контекста третий') 
    five_content_text_three = models.TextField(max_length=456, unique=True, verbose_name='Текст третий контекста') 
    five_content_title_fo = models.CharField(max_length=256, unique=True, verbose_name='Заголовок контекста четвертый')
    # --------------------------------------------------------------------------------------------------------------------------
    five_button = models.CharField(max_length=256, unique=True, verbose_name='Текст первой кнопки')
    five_button_two = models.CharField(max_length=256, unique=True, verbose_name='Текст второй кнопки')
    # --------------------------------------------------------------------------------------------------------------------------
    five_modal_title = models.CharField(max_length=256, unique=True, verbose_name='Заголовок модального окна')
    five_image_one = models.ImageField(upload_to='articles_images', verbose_name='Первое изображение модального окна') 
    five_modal_description = models.CharField(max_length=256, unique=True, verbose_name='Второое описание модального окна')

    five_modal_title_t = models.CharField(max_length=256, unique=True, verbose_name='Заголовок модального окна')
    five_image_one_t = models.ImageField(upload_to='articles_images', verbose_name='Первое изображение модального окна') 
    five_image_two_t = models.ImageField(upload_to='articles_images', verbose_name='Второе изображение модального окна') 
    five_modal_title_min_t = models.CharField(max_length=256, unique=True, verbose_name='Второй заголовок модального окна')
    five_modal_description_t = models.CharField(max_length=256, unique=True, verbose_name='Второое описание модального окна')

    five_modal_title_r = models.CharField(max_length=256, unique=True, verbose_name='Заголовок модального окна')
    five_image_one_r = models.ImageField(upload_to='articles_images', verbose_name='Первое изображение модального окна') 
    five_image_two_r = models.ImageField(upload_to='articles_images', verbose_name='Второе изображение модального окна') 
    five_modal_title_min_r = models.CharField(max_length=256, unique=True, verbose_name='Второй заголовок модального окна')
    five_modal_description_r = models.CharField(max_length=256, unique=True, verbose_name='Второое описание модального окна')

    five_modal_title_e = models.CharField(max_length=256, unique=True, verbose_name='Заголовок модального окна')
    five_image_one_e = models.ImageField(upload_to='articles_images', verbose_name='Первое изображение модального окна') 
    five_modal_title_min_e = models.CharField(max_length=256, unique=True, verbose_name='Второй заголовок модального окна')
    five_modal_description_e = models.CharField(max_length=256, unique=True, verbose_name='Второое описание модального окна')

    def __str__(self):
        return self.title_about

    class Meta:
        verbose_name = 'Пятая страница упражнений'
        verbose_name_plural = 'Пятая страница упражнений'     





# ---------------------------------------------------------------------------------------------------------
class Six(models.Model):
    title_about = models.CharField(max_length=256, unique=True, verbose_name='Заголовок about') 
    title_image = models.ImageField(upload_to='articles_images', verbose_name='Изображение title') 
    logo_image = models.ImageField(upload_to='articles_images', verbose_name='Изображение логотипа') 
    header_logo_one = models.CharField(max_length=126, unique=True, verbose_name='Текст первой части логотипа') 
    header_logo_two = models.CharField(max_length=126, unique=True, verbose_name='Текст второй части логотипа')
    about_title = models.CharField(max_length=126, unique=True, verbose_name='Текст первой вкладки меню')
    about_title_two = models.CharField(max_length=126, unique=True, verbose_name='Текст второй вкладки меню')
    about_title_three = models.CharField(max_length=126, unique=True, verbose_name='Текст третей вкладки меню')
    burger_title = models.CharField(max_length=126, unique=True, verbose_name='Текст в бургер  меню')
    about_images = models.CharField(max_length=126, unique=True, verbose_name='Главный текст в about_images')
    about_images_title = models.CharField(max_length=126, unique=True, verbose_name='Втрой текст в about_images')
    about_images_text = models.CharField(max_length=126, unique=True, verbose_name='Третий текст в about_images')
    # ---------------------------------------------------------------------------------------------------------------------
    six_title = models.CharField(max_length=256, unique=True, verbose_name='Заголовок категорий') 
    # ----------------------------------------------------------------------------------------------------------------------
    six_title_one = models.CharField(max_length=256, unique=True, verbose_name='Текст первой категории') 
    six_title_two = models.CharField(max_length=256, unique=True, verbose_name='Текст второй категории') 
    six_title_three = models.CharField(max_length=256, unique=True, verbose_name='Текст третий категории') 
    six_title_fo = models.CharField(max_length=256, unique=True, verbose_name='Текст четвертой категории') 
    six_title_five = models.CharField(max_length=256, unique=True, verbose_name='Текст пятой категории') 
    six_title_six = models.CharField(max_length=256, unique=True, verbose_name='Текст шестой категории') 
    # ----------------------------------------------------------------------------------------------------------------------

    six_content_title = models.CharField(max_length=256, unique=True, verbose_name='Заголовок контекста первый') 
    six_content_text = models.TextField(max_length=456, unique=True, verbose_name='Текст первый контекста') 
    six_content_title_two = models.CharField(max_length=256, unique=True, verbose_name='Заголовок контекста второй') 
    six_content_text_two = models.TextField(max_length=456, unique=True, verbose_name='Текст второй контекста') 
    six_content_title_three = models.CharField(max_length=256, unique=True, verbose_name='Заголовок контекста третий') 
    six_content_text_three = models.TextField(max_length=456, unique=True, verbose_name='Текст третий контекста') 
    six_content_title_fo = models.CharField(max_length=256, unique=True, verbose_name='Заголовок контекста четвертый')
    # --------------------------------------------------------------------------------------------------------------------------
    six_button = models.CharField(max_length=256, unique=True, verbose_name='Текст первой кнопки')
    six_button_two = models.CharField(max_length=256, unique=True, verbose_name='Текст второй кнопки')
    # --------------------------------------------------------------------------------------------------------------------------
    six_modal_title = models.CharField(max_length=256, unique=True, verbose_name='Заголовок модального окна')
    six_image_one = models.ImageField(upload_to='articles_images', verbose_name='Первое изображение модального окна') 
    six_image_two = models.ImageField(upload_to='articles_images', verbose_name='Второе изображение модального окна') 
    sixe_modal_title_min = models.CharField(max_length=256, unique=True, verbose_name='Второй заголовок модального окна')
    six_modal_description = models.CharField(max_length=256, unique=True, verbose_name='Второое описание модального окна')

    six_modal_title_t = models.CharField(max_length=256, unique=True, verbose_name='Заголовок модального окна')
    six_image_one_t = models.ImageField(upload_to='articles_images', verbose_name='Первое изображение модального окна') 
    six_image_two_t = models.ImageField(upload_to='articles_images', verbose_name='Второе изображение модального окна') 
    six_modal_title_min_t = models.CharField(max_length=256, unique=True, verbose_name='Второй заголовок модального окна')
    six_modal_description_t = models.CharField(max_length=256, unique=True, verbose_name='Второое описание модального окна')

    six_modal_title_r = models.CharField(max_length=256, unique=True, verbose_name='Заголовок модального окна')
    six_image_one_r = models.ImageField(upload_to='articles_images', verbose_name='Первое изображение модального окна') 
    six_image_two_r = models.ImageField(upload_to='articles_images', verbose_name='Второе изображение модального окна') 
    six_modal_title_min_r = models.CharField(max_length=256, unique=True, verbose_name='Второй заголовок модального окна')
    six_modal_description_r = models.CharField(max_length=256, unique=True, verbose_name='Второое описание модального окна')

    six_modal_title_e = models.CharField(max_length=256, unique=True, verbose_name='Заголовок модального окна')
    six_image_one_e = models.ImageField(upload_to='articles_images', verbose_name='Первое изображение модального окна') 
    six_image_two_e = models.ImageField(upload_to='articles_images', verbose_name='Второе изображение модального окна') 
    six_modal_title_min_e = models.CharField(max_length=256, unique=True, verbose_name='Второй заголовок модального окна')
    six_modal_description_e = models.CharField(max_length=256, unique=True, verbose_name='Второое описание модального окна')

    def __str__(self):
        return self.title_about

    class Meta:
        verbose_name = 'Шестая страница упражнений'
        verbose_name_plural = 'Шестая страница упражнений' 


class Message(models.Model):
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    recipient = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_from_admin = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.sender} -> {self.recipient}'