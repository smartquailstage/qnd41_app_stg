# Generated by Django 3.2.19 on 2023-07-15 02:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0025_alter_image_file_alter_rendition_file'),
        ('webapp', '0003_auto_20230713_1155'),
    ]

    operations = [
        migrations.AddField(
            model_name='galeriahome',
            name='image_17',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='logo_parther'),
        ),
        migrations.AddField(
            model_name='galeriahome',
            name='image_18',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='logo_parther'),
        ),
        migrations.AddField(
            model_name='galeriahome',
            name='image_19',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='logo_parther'),
        ),
        migrations.AddField(
            model_name='galeriahome',
            name='image_20',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='logo_parther'),
        ),
        migrations.AddField(
            model_name='galeriahome',
            name='image_21',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='logo_parther'),
        ),
        migrations.AddField(
            model_name='galeriahome',
            name='image_22',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='logo_parther'),
        ),
        migrations.AddField(
            model_name='galeriahome',
            name='image_23',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='logo_parther'),
        ),
        migrations.AddField(
            model_name='galeriahome',
            name='image_24',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='logo_parther'),
        ),
        migrations.AddField(
            model_name='galeriahome',
            name='image_25',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='logo_parther'),
        ),
        migrations.AddField(
            model_name='galeriahome',
            name='image_26',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='logo_parther'),
        ),
    ]