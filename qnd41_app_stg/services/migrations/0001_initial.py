# Generated by Django 3.2.22 on 2023-10-17 21:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('type', models.CharField(choices=[('danger', 'danger'), ('warning', 'warning'), ('info', 'info'), ('secondary', 'secondary'), ('default', 'default')], max_length=20, null=True)),
                ('logo', models.ImageField(blank=True, upload_to='logos/%Y/%m/%d')),
                ('description', models.TextField(blank=True)),
                ('video', models.URLField(null=True)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('slug', models.SlugField(max_length=200)),
                ('image', models.ImageField(blank=True, upload_to='products/%Y/%m/%d')),
                ('description', models.TextField(blank=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('serices_types', models.CharField(choices=[('Frontend', 'Frontend'), ('Backend', 'Backend')], max_length=20, null=True)),
                ('types', models.CharField(choices=[('primary', 'primary'), ('warning', 'warning'), ('success', 'success'), ('danger', 'danger')], max_length=20, null=True)),
                ('available', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='services.category')),
            ],
            options={
                'ordering': ('name',),
                'index_together': {('id', 'slug')},
            },
        ),
        migrations.CreateModel(
            name='CrewCategoryItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.ImageField(blank=True, upload_to='smartbusinesscrew/%Y/%m/%d')),
                ('nombre', models.CharField(db_index=True, max_length=200)),
                ('apellido', models.CharField(db_index=True, max_length=200)),
                ('edad', models.PositiveIntegerField(default=1)),
                ('años_experiencia', models.PositiveIntegerField(default=1)),
                ('about_me', models.TextField(blank=True)),
                ('email', models.EmailField(max_length=254)),
                ('insta', models.URLField(null=True)),
                ('face', models.URLField(null=True)),
                ('tiktok', models.URLField(null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='service', to='services.category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Service_Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('slug', models.SlugField(max_length=200)),
                ('image', models.ImageField(blank=True, upload_to='products/%Y/%m/%d')),
                ('description', models.TextField(blank=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('serices_types', models.CharField(choices=[('Frontend', 'Frontend'), ('Backend', 'Backend')], max_length=20, null=True)),
                ('types', models.CharField(choices=[('primary', 'primary'), ('warning', 'warning'), ('success', 'success'), ('danger', 'danger')], max_length=20, null=True)),
                ('available', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='services', to='services.product')),
            ],
            options={
                'ordering': ('name',),
                'index_together': {('id', 'slug')},
            },
        ),
    ]
