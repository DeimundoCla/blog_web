# Generated by Django 4.0.4 on 2022-07-02 19:31

from django.db import migrations, models
import django.db.models.deletion
import paramiko.pkey


class Migration(migrations.Migration):

    dependencies = [
        ('app_blog', '0016_alter_comentarios_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentarios',
            name='post',
            field=models.ForeignKey(default=paramiko.pkey.PKey, on_delete=django.db.models.deletion.CASCADE, related_name='comentario', to='app_blog.posteo'),
        ),
    ]