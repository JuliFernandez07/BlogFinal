# Generated by Django 3.2.15 on 2022-11-01 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppBlog', '0002_auto_20221101_0223'),
    ]

    operations = [
        migrations.RenameField(
            model_name='receta',
            old_name='autor',
            new_name='autor_nombre',
        ),
        migrations.AddField(
            model_name='receta',
            name='autor_usuario',
            field=models.CharField(default='', max_length=100),
        ),
    ]
