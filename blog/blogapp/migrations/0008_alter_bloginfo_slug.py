# Generated by Django 4.2 on 2023-10-29 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0007_bloginfo_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bloginfo',
            name='slug',
            field=models.SlugField(default=1, unique=True),
        ),
    ]