# Generated by Django 3.1.14 on 2022-09-27 12:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20220927_1321'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='author',
            new_name='auth',
        ),
    ]
