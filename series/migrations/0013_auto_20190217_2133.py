# Generated by Django 2.1.7 on 2019-02-17 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('series', '0012_auto_20190217_2132'),
    ]

    operations = [
        migrations.AddField(
            model_name='tvshow',
            name='country',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='tvshow',
            name='genres',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='tvshow',
            name='image',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='tvshow',
            name='language',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='tvshow',
            name='network',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='tvshow',
            name='nextepisode',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='tvshow',
            name='premiered',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='tvshow',
            name='runtime',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='tvshow',
            name='scheduled',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='tvshow',
            name='show_id',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]