# Generated by Django 4.2 on 2023-10-29 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0006_bloginfo_related_to'),
    ]

    operations = [
        migrations.AddField(
            model_name='bloginfo',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
    ]
