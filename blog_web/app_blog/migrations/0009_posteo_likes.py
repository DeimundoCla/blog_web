# Generated by Django 4.0.4 on 2022-06-29 01:09

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_blog', '0008_alter_posteo_contenido'),
    ]

    operations = [
        migrations.AddField(
            model_name='posteo',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='like', to=settings.AUTH_USER_MODEL),
        ),
    ]
