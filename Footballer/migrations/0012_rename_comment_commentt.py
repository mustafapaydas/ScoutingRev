# Generated by Django 3.2 on 2021-05-01 22:52

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Footballer', '0011_alter_comment_author'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comment',
            new_name='Commentt',
        ),
    ]
