# Generated by Django 3.2.19 on 2023-08-12 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sblshop', '0005_alter_sblproduct_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sblproduct',
            name='icon',
            field=models.CharField(blank=True, choices=[('icofont-legal', 'icofont-legal'), ('icofont-law-book', 'icofont-law-book'), ('icofont-ebook', 'icofont-ebook'), ('icofont-ui-office', 'icofont-ui-office'), ('icofont-list', 'icofont-list'), ('icofont-key', 'icofont-key')], db_index=True, max_length=200, null=True),
        ),
    ]
