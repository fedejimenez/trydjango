# Generated by Django 2.1.7 on 2019-02-17 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('series', '0014_auto_20190217_2141'),
    ]

    operations = [
        migrations.AddField(
            model_name='tvshow',
            name='genres_spaced',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]