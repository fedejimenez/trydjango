# Generated by Django 2.1.5 on 2019-02-09 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('series', '0007_auto_20190209_1244'),
    ]

    operations = [
        migrations.AddField(
            model_name='tvshow',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]