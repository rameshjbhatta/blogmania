# Generated by Django 4.2 on 2023-10-29 03:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0009_alter_bloginfo_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bloginfo',
            name='slug',
        ),
    ]
