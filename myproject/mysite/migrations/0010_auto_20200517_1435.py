# Generated by Django 2.2 on 2020-05-17 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0009_category_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(default='', upload_to='category', verbose_name='Изображение'),
        ),
    ]
