# Generated by Django 2.2 on 2020-05-17 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0010_auto_20200517_1435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(null=True, upload_to='category', verbose_name='Изображение'),
        ),
    ]
