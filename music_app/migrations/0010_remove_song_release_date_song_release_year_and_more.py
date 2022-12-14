# Generated by Django 4.1.1 on 2022-11-19 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_app', '0009_remove_artist_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='release_date',
        ),
        migrations.AddField(
            model_name='song',
            name='release_year',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='artist',
            name='age',
            field=models.IntegerField(null=True, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='artist',
            name='label',
            field=models.CharField(max_length=200, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='artist',
            name='name',
            field=models.CharField(max_length=100, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='artist',
            name='nationality',
            field=models.CharField(max_length=200, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='artist',
            name='website',
            field=models.CharField(max_length=100, verbose_name=''),
        ),
    ]
