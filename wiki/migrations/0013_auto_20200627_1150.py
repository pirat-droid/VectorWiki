# Generated by Django 3.0.7 on 2020-06-27 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0012_auto_20200627_1150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phonemodel',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='Email адрес'),
        ),
    ]
