# Generated by Django 2.2.16 on 2022-10-05 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_auto_20221005_0927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='bio',
            field=models.TextField(null=True, verbose_name='Биография'),
        ),
    ]
