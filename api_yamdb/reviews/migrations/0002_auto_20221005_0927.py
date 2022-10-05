# Generated by Django 2.2.16 on 2022-10-05 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='bio',
            field=models.TextField(default=' ', verbose_name='Биография'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='is_superuser',
            field=models.BooleanField(default=False, verbose_name='Является суперпользователем'),
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('user', 'User'), ('moder', 'Moderator'), ('admin', 'Admin')], default='user', max_length=5, verbose_name='Роль на сайте'),
        ),
    ]
