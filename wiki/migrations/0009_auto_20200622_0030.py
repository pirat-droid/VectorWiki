# Generated by Django 3.0.7 on 2020-06-21 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0008_auto_20200622_0023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='img',
            field=models.ImageField(default='images/images.jpg', upload_to='images/', verbose_name='Логотип'),
        ),
    ]
