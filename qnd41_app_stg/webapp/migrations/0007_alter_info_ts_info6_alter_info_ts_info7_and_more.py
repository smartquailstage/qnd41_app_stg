# Generated by Django 4.0.10 on 2024-06-27 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0006_galeriadeimagenes_banner_background_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='TS_info6',
            field=models.CharField(blank=True, max_length=350, null=True, verbose_name='Subtitulo de parrafo'),
        ),
        migrations.AlterField(
            model_name='info',
            name='TS_info7',
            field=models.CharField(blank=True, max_length=350, null=True, verbose_name='Subtitulo de parrafo-2'),
        ),
        migrations.AlterField(
            model_name='info',
            name='TS_info8',
            field=models.CharField(blank=True, max_length=350, null=True, verbose_name='Subtitulo de parrafo-3'),
        ),
    ]
