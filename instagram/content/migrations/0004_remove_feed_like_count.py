# Generated by Django 3.2.18 on 2023-05-27 13:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0003_bookmark_like_reply'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feed',
            name='like_count',
        ),
    ]
