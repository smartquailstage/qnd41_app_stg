# Generated by Django 4.0.10 on 2024-06-27 00:06

from django.db import migrations
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_info_ts_info3_info_author_name_info_bio3_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='info_title12',
            field=wagtail.fields.RichTextField(blank=True, verbose_name='Descripcion de producto'),
        ),
    ]