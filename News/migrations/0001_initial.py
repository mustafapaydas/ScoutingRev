# Generated by Django 3.2 on 2021-05-22 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='New',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('baslik1', models.CharField(max_length=50, verbose_name='Başlık')),
                ('resim1', models.FileField(max_length=25, upload_to='', verbose_name='Haber Resmi')),
                ('yazi', models.TextField(max_length=350, verbose_name='Haber')),
                ('tarih', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
