# Generated by Django 3.1.4 on 2020-12-20 17:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dedicated_page', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='title',
        ),
    ]
