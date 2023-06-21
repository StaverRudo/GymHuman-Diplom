# Generated by Django 3.2.13 on 2023-06-08 08:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_auto_20230605_1801'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleAdd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('info', models.TextField()),
                ('img_one', models.ImageField(upload_to='articles_images')),
                ('img_two', models.ImageField(upload_to='articles_images')),
                ('title_mini', models.CharField(max_length=256)),
                ('info_mini', models.TextField()),
            ],
            options={
                'verbose_name': 'Наполнение контентом статьи',
                'verbose_name_plural': 'Наполнение контентом статьи',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='add',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='articles.articleadd'),
        ),
    ]
