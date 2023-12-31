# Generated by Django 3.2.13 on 2023-06-11 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0012_auto_20230609_1941'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_about', models.CharField(max_length=256, unique=True, verbose_name='Заголовок about')),
                ('title_image', models.ImageField(upload_to='articles_images', verbose_name='Изображение title')),
                ('logo_image', models.ImageField(upload_to='articles_images', verbose_name='Изображение логотипа')),
                ('header_logo_one', models.CharField(max_length=126, unique=True, verbose_name='Текст первой части логотипа')),
                ('header_logo_two', models.CharField(max_length=126, unique=True, verbose_name='Текст второй части логотипа')),
                ('about_title', models.CharField(max_length=126, unique=True, verbose_name='Текст первой вкладки меню')),
                ('about_title_two', models.CharField(max_length=126, unique=True, verbose_name='Текст второй вкладки меню')),
                ('about_title_three', models.CharField(max_length=126, unique=True, verbose_name='Текст третей вкладки меню')),
                ('burger_title', models.CharField(max_length=126, unique=True, verbose_name='Текст в бургер  меню')),
                ('about_images', models.CharField(max_length=126, unique=True, verbose_name='Главный текст в about_images')),
                ('about_images_title', models.CharField(max_length=126, unique=True, verbose_name='Втрой текст в about_images')),
                ('about_images_text', models.CharField(max_length=126, unique=True, verbose_name='Третий текст в about_images')),
                ('profile_more_text', models.CharField(max_length=126, unique=True, verbose_name='Второй текст в профиле')),
                ('strelka_image', models.ImageField(upload_to='articles_images', verbose_name='Изображение для возврата в начало сайта')),
                ('sidebar_input', models.CharField(max_length=126, unique=True, verbose_name='Текст в placeholder поиска')),
                ('sidebar_button', models.CharField(max_length=126, unique=True, verbose_name='Текст кнопки поиска')),
                ('sidebar_title', models.CharField(max_length=126, unique=True, verbose_name='Заголовок категорий')),
                ('sidebar_arhive_titile', models.CharField(max_length=126, unique=True, verbose_name='Заголовок архива')),
                ('sidebar_comments_title', models.CharField(max_length=126, unique=True, verbose_name='Заголовок последних комментариев')),
                ('content_buttonblock_button', models.CharField(max_length=126, unique=True, verbose_name='Текст кнопки показа следующий статей')),
                ('modal_title', models.CharField(max_length=126, unique=True, verbose_name='Заголовок формы')),
                ('modal_form_top_tile_one', models.CharField(max_length=126, unique=True, verbose_name='Первое поле input формы')),
                ('modal_form_top_tile_two', models.CharField(max_length=126, unique=True, verbose_name='Второе поле input формы')),
                ('modal_form_top_tile_three', models.CharField(max_length=126, unique=True, verbose_name='Третье поле input формы')),
                ('modal_form_top_tile_fo', models.CharField(max_length=126, unique=True, verbose_name='Четвертое поле input формы')),
                ('modal_form_top_tile_five', models.CharField(max_length=126, unique=True, verbose_name='Пятое поле input формы')),
                ('index_btn', models.CharField(max_length=126, unique=True, verbose_name='Текст кнопки формы')),
                ('button_look', models.ImageField(upload_to='articles_images', verbose_name='Изображение бокового меню')),
                ('right_bar_images_one', models.ImageField(upload_to='articles_images', verbose_name='Первое изображение бокового меню')),
                ('right_bar_images_two', models.ImageField(upload_to='articles_images', verbose_name='Второе изображение бокового меню')),
                ('right_bar_images_three', models.ImageField(upload_to='articles_images', verbose_name='Третье изображение бокового меню')),
                ('right_bar_images_fo', models.ImageField(upload_to='articles_images', verbose_name='Четвертое изображение бокового меню')),
            ],
        ),
    ]
