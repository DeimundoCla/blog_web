# Generated by Django 4.0.4 on 2022-07-03 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_blog', '0019_alter_perfil_user_alter_posteo_contenido_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posteo',
            name='imagen',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
