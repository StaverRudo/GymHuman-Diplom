# Generated by Django 3.2.13 on 2023-06-05 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_home'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='home',
            options={'verbose_name': 'Главная страница', 'verbose_name_plural': 'Главная страница'},
        ),
        migrations.AlterField(
            model_name='home',
            name='footer_title',
            field=models.CharField(max_length=256, unique=True, verbose_name='Заголовок блока footer'),
        ),
        migrations.AlterField(
            model_name='home',
            name='info_description',
            field=models.TextField(verbose_name='Описание к блоку info'),
        ),
        migrations.AlterField(
            model_name='home',
            name='info_title',
            field=models.CharField(max_length=256, unique=True, verbose_name='Заголовок блока info'),
        ),
        migrations.AlterField(
            model_name='home',
            name='infoblock_card_description_one',
            field=models.TextField(verbose_name='Первое описание блока info'),
        ),
        migrations.AlterField(
            model_name='home',
            name='infoblock_card_description_three',
            field=models.TextField(verbose_name='Третье описание блока info'),
        ),
        migrations.AlterField(
            model_name='home',
            name='infoblock_card_description_two',
            field=models.TextField(verbose_name='Второе описание блока info'),
        ),
        migrations.AlterField(
            model_name='home',
            name='infoblock_card_image_one',
            field=models.ImageField(upload_to='articles_images', verbose_name='Первое изображение блока info'),
        ),
        migrations.AlterField(
            model_name='home',
            name='infoblock_card_image_three',
            field=models.ImageField(upload_to='articles_images', verbose_name='Третье изображение блока info'),
        ),
        migrations.AlterField(
            model_name='home',
            name='infoblock_card_image_two',
            field=models.ImageField(upload_to='articles_images', verbose_name='Второе изображение блока info'),
        ),
        migrations.AlterField(
            model_name='home',
            name='infoblock_card_title_one',
            field=models.CharField(max_length=256, unique=True, verbose_name='Первый заголовок блока info'),
        ),
        migrations.AlterField(
            model_name='home',
            name='infoblock_card_title_three',
            field=models.CharField(max_length=126, unique=True, verbose_name='Третий заголовок блока info'),
        ),
        migrations.AlterField(
            model_name='home',
            name='infoblock_card_title_two',
            field=models.CharField(max_length=126, unique=True, verbose_name='Второй заголовок блока info'),
        ),
        migrations.AlterField(
            model_name='home',
            name='login_text_one',
            field=models.CharField(max_length=256, unique=True, verbose_name='Первая кнопка входа'),
        ),
        migrations.AlterField(
            model_name='home',
            name='login_text_two',
            field=models.CharField(max_length=256, unique=True, verbose_name='Вторая кнопка входа'),
        ),
        migrations.AlterField(
            model_name='home',
            name='logo_image',
            field=models.ImageField(upload_to='articles_images', verbose_name='Изображение логотипа'),
        ),
        migrations.AlterField(
            model_name='home',
            name='slider_button_one',
            field=models.CharField(max_length=256, unique=True, verbose_name='Первая кнопка на слайдере'),
        ),
        migrations.AlterField(
            model_name='home',
            name='slider_button_two',
            field=models.CharField(max_length=256, unique=True, verbose_name='Второе изображение слайдера'),
        ),
        migrations.AlterField(
            model_name='home',
            name='slider_image_one',
            field=models.ImageField(upload_to='articles_images', verbose_name='Первое изображение слайдера'),
        ),
        migrations.AlterField(
            model_name='home',
            name='slider_image_two',
            field=models.ImageField(upload_to='articles_images', verbose_name='Второе изображение слайдера'),
        ),
        migrations.AlterField(
            model_name='home',
            name='slider_text_one',
            field=models.CharField(max_length=256, unique=True, verbose_name='Первый текст на слайдере'),
        ),
        migrations.AlterField(
            model_name='home',
            name='slider_text_two',
            field=models.CharField(max_length=256, unique=True, verbose_name='Второй текст на слайдере'),
        ),
        migrations.AlterField(
            model_name='home',
            name='strelka_image',
            field=models.ImageField(upload_to='articles_images', verbose_name='Изображение для возврата в начало сайта'),
        ),
        migrations.AlterField(
            model_name='home',
            name='title',
            field=models.CharField(max_length=256, unique=True, verbose_name='Заголовок сайта'),
        ),
        migrations.AlterField(
            model_name='home',
            name='title_image',
            field=models.ImageField(upload_to='articles_images', verbose_name='Изображение зоголовка сайта'),
        ),
        migrations.AlterField(
            model_name='home',
            name='title_logo_one',
            field=models.CharField(max_length=126, unique=True, verbose_name='Текст первой части логотипа'),
        ),
        migrations.AlterField(
            model_name='home',
            name='title_logo_two',
            field=models.CharField(max_length=126, unique=True, verbose_name='Текст второй части логотипа'),
        ),
        migrations.AlterField(
            model_name='home',
            name='tools_item_image_one',
            field=models.ImageField(upload_to='articles_images', verbose_name='Первое изображение карточки блока tools'),
        ),
        migrations.AlterField(
            model_name='home',
            name='tools_item_image_three',
            field=models.ImageField(upload_to='articles_images', verbose_name='Третье изображение карточки блока tools'),
        ),
        migrations.AlterField(
            model_name='home',
            name='tools_item_image_two',
            field=models.ImageField(upload_to='articles_images', verbose_name='Второе изображение карточки блока tools'),
        ),
        migrations.AlterField(
            model_name='home',
            name='tools_item_text_one',
            field=models.TextField(verbose_name='Описание первой карточки блока tools'),
        ),
        migrations.AlterField(
            model_name='home',
            name='tools_item_text_three',
            field=models.TextField(verbose_name='Описание третей карточки блока tools'),
        ),
        migrations.AlterField(
            model_name='home',
            name='tools_item_text_two',
            field=models.TextField(verbose_name='Описание второй карточки блока tools'),
        ),
        migrations.AlterField(
            model_name='home',
            name='tools_item_title_one',
            field=models.CharField(max_length=256, unique=True, verbose_name='Первый заголовок карточки блока tools'),
        ),
        migrations.AlterField(
            model_name='home',
            name='tools_item_title_three',
            field=models.CharField(max_length=256, unique=True, verbose_name='Третий заголовок карточки блока tools'),
        ),
        migrations.AlterField(
            model_name='home',
            name='tools_item_title_two',
            field=models.CharField(max_length=256, unique=True, verbose_name='Второй заголовок карточки блока tools'),
        ),
        migrations.AlterField(
            model_name='home',
            name='tools_text',
            field=models.TextField(verbose_name='Описание блока tools'),
        ),
        migrations.AlterField(
            model_name='home',
            name='tools_title',
            field=models.CharField(max_length=256, unique=True, verbose_name='Заголовок блока tools'),
        ),
    ]
