# Generated by Django 4.2 on 2023-04-11 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='img.jpg', upload_to='image/%Y', verbose_name='Изображения'),
            preserve_default=False,
        ),
    ]
