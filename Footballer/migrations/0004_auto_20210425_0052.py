# Generated by Django 3.2 on 2021-04-24 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Footballer', '0003_footballer_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='footballer',
            name='image1',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Fotoğraf ekleme'),
        ),
        migrations.AddField(
            model_name='footballer',
            name='image2',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Fotoğraf ekleme'),
        ),
        migrations.AddField(
            model_name='footballer',
            name='image3',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Fotoğraf ekleme'),
        ),
    ]
