# Generated by Django 4.2.2 on 2023-06-10 00:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cabin_home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='auther',
            new_name='author',
        ),
    ]
