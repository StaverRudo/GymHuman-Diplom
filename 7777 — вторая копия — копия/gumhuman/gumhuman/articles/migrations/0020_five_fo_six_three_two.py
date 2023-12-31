# Generated by Django 3.2.13 on 2023-06-16 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0019_one'),
    ]

    operations = [
        migrations.CreateModel(
            name='Five',
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
                ('five_title', models.CharField(max_length=256, unique=True, verbose_name='Заголовок категорий')),
                ('five_title_one', models.CharField(max_length=256, unique=True, verbose_name='Текст первой категории')),
                ('five_title_two', models.CharField(max_length=256, unique=True, verbose_name='Текст второй категории')),
                ('five_title_three', models.CharField(max_length=256, unique=True, verbose_name='Текст третий категории')),
                ('five_title_fo', models.CharField(max_length=256, unique=True, verbose_name='Текст четвертой категории')),
                ('five_title_five', models.CharField(max_length=256, unique=True, verbose_name='Текст пятой категории')),
                ('five_title_six', models.CharField(max_length=256, unique=True, verbose_name='Текст шестой категории')),
                ('five_content_title', models.CharField(max_length=256, unique=True, verbose_name='Заголовок контекста первый')),
                ('five_content_text', models.TextField(max_length=456, unique=True, verbose_name='Текст первый контекста')),
                ('five_content_title_two', models.CharField(max_length=256, unique=True, verbose_name='Заголовок контекста второй')),
                ('five_content_text_two', models.TextField(max_length=456, unique=True, verbose_name='Текст второй контекста')),
                ('five_content_title_three', models.CharField(max_length=256, unique=True, verbose_name='Заголовок контекста третий')),
                ('five_content_text_three', models.TextField(max_length=456, unique=True, verbose_name='Текст третий контекста')),
                ('five_content_title_fo', models.CharField(max_length=256, unique=True, verbose_name='Заголовок контекста четвертый')),
                ('five_button', models.CharField(max_length=256, unique=True, verbose_name='Текст первой кнопки')),
                ('five_button_two', models.CharField(max_length=256, unique=True, verbose_name='Текст второй кнопки')),
                ('five_modal_title', models.CharField(max_length=256, unique=True, verbose_name='Заголовок модального окна')),
                ('five_image_one', models.ImageField(upload_to='articles_images', verbose_name='Первое изображение модального окна')),
                ('five_modal_description', models.CharField(max_length=256, unique=True, verbose_name='Второое описание модального окна')),
                ('five_modal_title_t', models.CharField(max_length=256, unique=True, verbose_name='Заголовок модального окна')),
                ('five_image_one_t', models.ImageField(upload_to='articles_images', verbose_name='Первое изображение модального окна')),
                ('five_image_two_t', models.ImageField(upload_to='articles_images', verbose_name='Второе изображение модального окна')),
                ('five_modal_title_min_t', models.CharField(max_length=256, unique=True, verbose_name='Второй заголовок модального окна')),
                ('five_modal_description_t', models.CharField(max_length=256, unique=True, verbose_name='Второое описание модального окна')),
                ('five_modal_title_r', models.CharField(max_length=256, unique=True, verbose_name='Заголовок модального окна')),
                ('five_image_one_r', models.ImageField(upload_to='articles_images', verbose_name='Первое изображение модального окна')),
                ('five_image_two_r', models.ImageField(upload_to='articles_images', verbose_name='Второе изображение модального окна')),
                ('five_modal_title_min_r', models.CharField(max_length=256, unique=True, verbose_name='Второй заголовок модального окна')),
                ('five_modal_description_r', models.CharField(max_length=256, unique=True, verbose_name='Второое описание модального окна')),
                ('five_modal_title_e', models.CharField(max_length=256, unique=True, verbose_name='Заголовок модального окна')),
                ('five_image_one_e', models.ImageField(upload_to='articles_images', verbose_name='Первое изображение модального окна')),
                ('five_modal_title_min_e', models.CharField(max_length=256, unique=True, verbose_name='Второй заголовок модального окна')),
                ('five_modal_description_e', models.CharField(max_length=256, unique=True, verbose_name='Второое описание модального окна')),
            ],
            options={
                'verbose_name': 'Пятая страница упражнений',
                'verbose_name_plural': 'Пятая страница упражнений',
            },
        ),
        migrations.CreateModel(
            name='Fo',
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
                ('fo_title', models.CharField(max_length=256, unique=True, verbose_name='Заголовок категорий')),
                ('fo_title_one', models.CharField(max_length=256, unique=True, verbose_name='Текст первой категории')),
                ('fo_title_two', models.CharField(max_length=256, unique=True, verbose_name='Текст второй категории')),
                ('fo_title_three', models.CharField(max_length=256, unique=True, verbose_name='Текст третий категории')),
                ('fo_title_fo', models.CharField(max_length=256, unique=True, verbose_name='Текст четвертой категории')),
                ('fo_title_five', models.CharField(max_length=256, unique=True, verbose_name='Текст пятой категории')),
                ('fo_title_six', models.CharField(max_length=256, unique=True, verbose_name='Текст шестой категории')),
                ('fo_content_title', models.CharField(max_length=256, unique=True, verbose_name='Заголовок контекста первый')),
                ('fo_content_text', models.TextField(max_length=456, unique=True, verbose_name='Текст первый контекста')),
                ('fo_content_title_two', models.CharField(max_length=256, unique=True, verbose_name='Заголовок контекста второй')),
                ('fo_content_text_two', models.TextField(max_length=456, unique=True, verbose_name='Текст второй контекста')),
                ('fo_content_title_three', models.CharField(max_length=256, unique=True, verbose_name='Заголовок контекста третий')),
                ('fo_content_text_three', models.TextField(max_length=456, unique=True, verbose_name='Текст третий контекста')),
                ('fo_content_title_fo', models.CharField(max_length=256, unique=True, verbose_name='Заголовок контекста четвертый')),
                ('fo_button', models.CharField(max_length=256, unique=True, verbose_name='Текст первой кнопки')),
                ('fo_button_two', models.CharField(max_length=256, unique=True, verbose_name='Текст второй кнопки')),
                ('fo_modal_title', models.CharField(max_length=256, unique=True, verbose_name='Заголовок модального окна')),
                ('fo_image_one', models.ImageField(upload_to='articles_images', verbose_name='Первое изображение модального окна')),
                ('fo_modal_title_min', models.CharField(max_length=256, unique=True, verbose_name='Второй заголовок модального окна')),
                ('fo_modal_description', models.CharField(max_length=256, unique=True, verbose_name='Второое описание модального окна')),
                ('fo_modal_title_t', models.CharField(max_length=256, unique=True, verbose_name='Заголовок модального окна')),
                ('fo_image_one_t', models.ImageField(upload_to='articles_images', verbose_name='Первое изображение модального окна')),
                ('fo_image_two_t', models.ImageField(upload_to='articles_images', verbose_name='Второе изображение модального окна')),
                ('fo_modal_title_min_t', models.CharField(max_length=256, unique=True, verbose_name='Второй заголовок модального окна')),
                ('fo_modal_description_t', models.CharField(max_length=256, unique=True, verbose_name='Второое описание модального окна')),
                ('fo_modal_title_r', models.CharField(max_length=256, unique=True, verbose_name='Заголовок модального окна')),
                ('fo_image_one_r', models.ImageField(upload_to='articles_images', verbose_name='Первое изображение модального окна')),
                ('fo_image_two_r', models.ImageField(upload_to='articles_images', verbose_name='Второе изображение модального окна')),
                ('fo_modal_title_min_r', models.CharField(max_length=256, unique=True, verbose_name='Второй заголовок модального окна')),
                ('fo_modal_description_r', models.CharField(max_length=256, unique=True, verbose_name='Второое описание модального окна')),
                ('fo_modal_title_e', models.CharField(max_length=256, unique=True, verbose_name='Заголовок модального окна')),
                ('fo_image_one_e', models.ImageField(upload_to='articles_images', verbose_name='Первое изображение модального окна')),
                ('fo_modal_title_min_e', models.CharField(max_length=256, unique=True, verbose_name='Второй заголовок модального окна')),
                ('fo_modal_description_e', models.CharField(max_length=256, unique=True, verbose_name='Второое описание модального окна')),
            ],
            options={
                'verbose_name': 'Четвертая страница упражнений',
                'verbose_name_plural': 'Четвертая страница упражнений',
            },
        ),
        migrations.CreateModel(
            name='Six',
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
                ('six_title', models.CharField(max_length=256, unique=True, verbose_name='Заголовок категорий')),
                ('six_title_one', models.CharField(max_length=256, unique=True, verbose_name='Текст первой категории')),
                ('six_title_two', models.CharField(max_length=256, unique=True, verbose_name='Текст второй категории')),
                ('six_title_three', models.CharField(max_length=256, unique=True, verbose_name='Текст третий категории')),
                ('six_title_fo', models.CharField(max_length=256, unique=True, verbose_name='Текст четвертой категории')),
                ('six_title_five', models.CharField(max_length=256, unique=True, verbose_name='Текст пятой категории')),
                ('six_title_six', models.CharField(max_length=256, unique=True, verbose_name='Текст шестой категории')),
                ('six_content_title', models.CharField(max_length=256, unique=True, verbose_name='Заголовок контекста первый')),
                ('six_content_text', models.TextField(max_length=456, unique=True, verbose_name='Текст первый контекста')),
                ('six_content_title_two', models.CharField(max_length=256, unique=True, verbose_name='Заголовок контекста второй')),
                ('six_content_text_two', models.TextField(max_length=456, unique=True, verbose_name='Текст второй контекста')),
                ('six_content_title_three', models.CharField(max_length=256, unique=True, verbose_name='Заголовок контекста третий')),
                ('six_content_text_three', models.TextField(max_length=456, unique=True, verbose_name='Текст третий контекста')),
                ('six_content_title_fo', models.CharField(max_length=256, unique=True, verbose_name='Заголовок контекста четвертый')),
                ('six_button', models.CharField(max_length=256, unique=True, verbose_name='Текст первой кнопки')),
                ('six_button_two', models.CharField(max_length=256, unique=True, verbose_name='Текст второй кнопки')),
                ('six_modal_title', models.CharField(max_length=256, unique=True, verbose_name='Заголовок модального окна')),
                ('six_image_one', models.ImageField(upload_to='articles_images', verbose_name='Первое изображение модального окна')),
                ('six_image_two', models.ImageField(upload_to='articles_images', verbose_name='Второе изображение модального окна')),
                ('sixe_modal_title_min', models.CharField(max_length=256, unique=True, verbose_name='Второй заголовок модального окна')),
                ('six_modal_description', models.CharField(max_length=256, unique=True, verbose_name='Второое описание модального окна')),
                ('six_modal_title_t', models.CharField(max_length=256, unique=True, verbose_name='Заголовок модального окна')),
                ('six_image_one_t', models.ImageField(upload_to='articles_images', verbose_name='Первое изображение модального окна')),
                ('six_image_two_t', models.ImageField(upload_to='articles_images', verbose_name='Второе изображение модального окна')),
                ('six_modal_title_min_t', models.CharField(max_length=256, unique=True, verbose_name='Второй заголовок модального окна')),
                ('six_modal_description_t', models.CharField(max_length=256, unique=True, verbose_name='Второое описание модального окна')),
                ('six_modal_title_r', models.CharField(max_length=256, unique=True, verbose_name='Заголовок модального окна')),
                ('six_image_one_r', models.ImageField(upload_to='articles_images', verbose_name='Первое изображение модального окна')),
                ('six_image_two_r', models.ImageField(upload_to='articles_images', verbose_name='Второе изображение модального окна')),
                ('six_modal_title_min_r', models.CharField(max_length=256, unique=True, verbose_name='Второй заголовок модального окна')),
                ('six_modal_description_r', models.CharField(max_length=256, unique=True, verbose_name='Второое описание модального окна')),
                ('six_modal_title_e', models.CharField(max_length=256, unique=True, verbose_name='Заголовок модального окна')),
                ('six_image_one_e', models.ImageField(upload_to='articles_images', verbose_name='Первое изображение модального окна')),
                ('six_image_two_e', models.ImageField(upload_to='articles_images', verbose_name='Второе изображение модального окна')),
                ('six_modal_title_min_e', models.CharField(max_length=256, unique=True, verbose_name='Второй заголовок модального окна')),
                ('six_modal_description_e', models.CharField(max_length=256, unique=True, verbose_name='Второое описание модального окна')),
            ],
            options={
                'verbose_name': 'Шестая страница упражнений',
                'verbose_name_plural': 'Шестая страница упражнений',
            },
        ),
        migrations.CreateModel(
            name='Three',
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
                ('three_title', models.CharField(max_length=256, unique=True, verbose_name='Заголовок категорий')),
                ('three_title_one', models.CharField(max_length=256, unique=True, verbose_name='Текст первой категории')),
                ('three_title_two', models.CharField(max_length=256, unique=True, verbose_name='Текст второй категории')),
                ('three_title_three', models.CharField(max_length=256, unique=True, verbose_name='Текст третий категории')),
                ('three_title_fo', models.CharField(max_length=256, unique=True, verbose_name='Текст четвертой категории')),
                ('three_title_five', models.CharField(max_length=256, unique=True, verbose_name='Текст пятой категории')),
                ('three_title_six', models.CharField(max_length=256, unique=True, verbose_name='Текст шестой категории')),
                ('three_content_title', models.CharField(max_length=256, unique=True, verbose_name='Заголовок контекста первый')),
                ('three_content_text', models.TextField(max_length=456, unique=True, verbose_name='Текст первый контекста')),
                ('three_content_title_two', models.CharField(max_length=256, unique=True, verbose_name='Заголовок контекста второй')),
                ('three_content_text_two', models.TextField(max_length=456, unique=True, verbose_name='Текст второй контекста')),
                ('three_content_title_three', models.CharField(max_length=256, unique=True, verbose_name='Заголовок контекста третий')),
                ('three_content_text_three', models.TextField(max_length=456, unique=True, verbose_name='Текст третий контекста')),
                ('three_content_title_fo', models.CharField(max_length=256, unique=True, verbose_name='Заголовок контекста четвертый')),
                ('three_button', models.CharField(max_length=256, unique=True, verbose_name='Текст первой кнопки')),
                ('three_button_two', models.CharField(max_length=256, unique=True, verbose_name='Текст второй кнопки')),
                ('three_modal_title', models.CharField(max_length=256, unique=True, verbose_name='Заголовок модального окна')),
                ('three_image_one', models.ImageField(upload_to='articles_images', verbose_name='Первое изображение модального окна')),
                ('three_image_two', models.ImageField(upload_to='articles_images', verbose_name='Второе изображение модального окна')),
                ('three_modal_title_min', models.CharField(max_length=256, unique=True, verbose_name='Второй заголовок модального окна')),
                ('three_modal_description', models.CharField(max_length=256, unique=True, verbose_name='Второое описание модального окна')),
                ('three_modal_title_t', models.CharField(max_length=256, unique=True, verbose_name='Заголовок модального окна')),
                ('three_image_one_t', models.ImageField(upload_to='articles_images', verbose_name='Первое изображение модального окна')),
                ('three_image_two_t', models.ImageField(upload_to='articles_images', verbose_name='Второе изображение модального окна')),
                ('three_modal_title_min_t', models.CharField(max_length=256, unique=True, verbose_name='Второй заголовок модального окна')),
                ('three_modal_description_t', models.CharField(max_length=256, unique=True, verbose_name='Второое описание модального окна')),
                ('three_modal_title_r', models.CharField(max_length=256, unique=True, verbose_name='Заголовок модального окна')),
                ('three_image_one_r', models.ImageField(upload_to='articles_images', verbose_name='Первое изображение модального окна')),
                ('three_image_two_r', models.ImageField(upload_to='articles_images', verbose_name='Второе изображение модального окна')),
                ('three_modal_title_min_r', models.CharField(max_length=256, unique=True, verbose_name='Второй заголовок модального окна')),
                ('three_modal_description_r', models.CharField(max_length=256, unique=True, verbose_name='Второое описание модального окна')),
                ('three_modal_title_e', models.CharField(max_length=256, unique=True, verbose_name='Заголовок модального окна')),
                ('three_image_one_e', models.ImageField(upload_to='articles_images', verbose_name='Первое изображение модального окна')),
                ('three_image_two_e', models.ImageField(upload_to='articles_images', verbose_name='Второе изображение модального окна')),
                ('three_modal_title_min_e', models.CharField(max_length=256, unique=True, verbose_name='Второй заголовок модального окна')),
                ('three_modal_description_e', models.CharField(max_length=256, unique=True, verbose_name='Второое описание модального окна')),
            ],
            options={
                'verbose_name': 'Третья страница упражнений',
                'verbose_name_plural': 'третья страница упражнений',
            },
        ),
        migrations.CreateModel(
            name='Two',
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
                ('two_title', models.CharField(max_length=256, unique=True, verbose_name='Заголовок категорий')),
                ('two_title_one', models.CharField(max_length=256, unique=True, verbose_name='Текст первой категории')),
                ('two_title_two', models.CharField(max_length=256, unique=True, verbose_name='Текст второй категории')),
                ('two_title_three', models.CharField(max_length=256, unique=True, verbose_name='Текст третий категории')),
                ('two_title_fo', models.CharField(max_length=256, unique=True, verbose_name='Текст четвертой категории')),
                ('two_title_five', models.CharField(max_length=256, unique=True, verbose_name='Текст пятой категории')),
                ('two_title_six', models.CharField(max_length=256, unique=True, verbose_name='Текст шестой категории')),
                ('two_content_title', models.CharField(max_length=256, unique=True, verbose_name='Заголовок контекста первый')),
                ('two_content_text', models.TextField(max_length=456, unique=True, verbose_name='Текст первый контекста')),
                ('two_content_title_two', models.CharField(max_length=256, unique=True, verbose_name='Заголовок контекста второй')),
                ('two_content_text_two', models.TextField(max_length=456, unique=True, verbose_name='Текст второй контекста')),
                ('two_content_title_three', models.CharField(max_length=256, unique=True, verbose_name='Заголовок контекста третий')),
                ('two_content_text_three', models.TextField(max_length=456, unique=True, verbose_name='Текст третий контекста')),
                ('two_content_title_fo', models.CharField(max_length=256, unique=True, verbose_name='Заголовок контекста четвертый')),
                ('two_button', models.CharField(max_length=256, unique=True, verbose_name='Текст первой кнопки')),
                ('two_button_two', models.CharField(max_length=256, unique=True, verbose_name='Текст второй кнопки')),
                ('two_modal_title', models.CharField(max_length=256, unique=True, verbose_name='Заголовок модального окна')),
                ('two_image_one', models.ImageField(upload_to='articles_images', verbose_name='Первое изображение модального окна')),
                ('two_image_two', models.ImageField(upload_to='articles_images', verbose_name='Второе изображение модального окна')),
                ('two_modal_title_min', models.CharField(max_length=256, unique=True, verbose_name='Второй заголовок модального окна')),
                ('two_modal_description', models.CharField(max_length=256, unique=True, verbose_name='Второое описание модального окна')),
                ('two_modal_title_t', models.CharField(max_length=256, unique=True, verbose_name='Заголовок модального окна')),
                ('two_image_one_t', models.ImageField(upload_to='articles_images', verbose_name='Первое изображение модального окна')),
                ('two_image_two_t', models.ImageField(upload_to='articles_images', verbose_name='Второе изображение модального окна')),
                ('two_modal_title_min_t', models.CharField(max_length=256, unique=True, verbose_name='Второй заголовок модального окна')),
                ('two_modal_description_t', models.CharField(max_length=256, unique=True, verbose_name='Второое описание модального окна')),
                ('two_modal_title_r', models.CharField(max_length=256, unique=True, verbose_name='Заголовок модального окна')),
                ('two_image_one_r', models.ImageField(upload_to='articles_images', verbose_name='Первое изображение модального окна')),
                ('two_image_two_r', models.ImageField(upload_to='articles_images', verbose_name='Второе изображение модального окна')),
                ('two_modal_title_min_r', models.CharField(max_length=256, unique=True, verbose_name='Второй заголовок модального окна')),
                ('two_modal_description_r', models.CharField(max_length=256, unique=True, verbose_name='Второое описание модального окна')),
                ('two_modal_title_e', models.CharField(max_length=256, unique=True, verbose_name='Заголовок модального окна')),
                ('two_image_one_e', models.ImageField(upload_to='articles_images', verbose_name='Первое изображение модального окна')),
                ('two_image_two_e', models.ImageField(upload_to='articles_images', verbose_name='Второе изображение модального окна')),
                ('two_modal_title_min_e', models.CharField(max_length=256, unique=True, verbose_name='Второй заголовок модального окна')),
                ('two_modal_description_e', models.CharField(max_length=256, unique=True, verbose_name='Второое описание модального окна')),
            ],
            options={
                'verbose_name': 'Вторая страница упражнений',
                'verbose_name_plural': 'Вторая страница упражнений',
            },
        ),
    ]
