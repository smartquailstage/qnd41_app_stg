# Generated by Django 3.2.19 on 2023-08-21 02:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sbaorders', '0001_initial'),
        ('sbashop', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SBLProduct',
            new_name='SBAProduct',
        ),
    ]
