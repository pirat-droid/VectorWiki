# Generated by Django 3.0.7 on 2020-06-11 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0005_auto_20200611_2106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='border',
            field=models.BooleanField(default=False, verbose_name='Доска'),
        ),
    ]
