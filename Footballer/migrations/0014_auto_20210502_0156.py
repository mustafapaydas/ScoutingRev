# Generated by Django 3.2 on 2021-05-01 22:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Footballer', '0013_auto_20210502_0154'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_content', models.TextField(max_length=250, verbose_name='Yorum')),
                ('comment_date', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Kullanıcı')),
                ('futbolcu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='Footballer.footballer', verbose_name='Futbolcu')),
            ],
        ),
        migrations.DeleteModel(
            name='Yorumlar',
        ),
    ]