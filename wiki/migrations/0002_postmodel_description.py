# Generated by Django 3.0.7 on 2020-06-09 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='postmodel',
            name='description',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
    ]
