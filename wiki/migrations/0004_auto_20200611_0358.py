# Generated by Django 3.0.7 on 2020-06-10 22:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0003_auto_20200609_0923'),
    ]

    operations = [
        migrations.RenameField(
            model_name='postmodel',
            old_name='url',
            new_name='slug',
        ),
    ]
