# Generated by Django 3.1.7 on 2021-03-11 13:59

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manage_library', '0010_auto_20210307_2158'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='manage_library.category'),
        ),
        migrations.AddField(
            model_name='book',
            name='cover',
            field=models.ImageField(default='covers/default_cover.jpg', upload_to='covers'),
        ),
        migrations.AlterField(
            model_name='book',
            name='isbn_number',
            field=models.CharField(max_length=13, validators=[django.core.validators.RegexValidator(message='Wrong ISBN length', regex='^[0-9]{10}$|^[0-9]{13}$')]),
        ),
        migrations.AlterField(
            model_name='book',
            name='shelf',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='manage_library.shelf'),
        ),
    ]
