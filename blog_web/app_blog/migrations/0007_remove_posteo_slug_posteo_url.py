# Generated by Django 4.0.4 on 2022-06-28 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_blog', '0006_alter_posteo_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posteo',
            name='slug',
        ),
        migrations.AddField(
            model_name='posteo',
            name='url',
            field=models.SlugField(max_length=264, null=True, unique=True),
        ),
    ]
