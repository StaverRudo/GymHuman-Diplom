# Generated by Django 3.2.13 on 2023-06-14 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0014_auto_20230612_0231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, default='cris2.jpg', null=True, upload_to='articles_images'),
        ),
    ]
