# Generated by Django 3.2.4 on 2021-06-17 16:53

import books.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_alter_book_series'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='picture',
            field=models.ImageField(default='Books/book0.png', upload_to=books.models.book_directory_path, verbose_name='Изображение'),
        ),
    ]
