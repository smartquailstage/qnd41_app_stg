# Generated by Django 3.2.19 on 2023-09-08 20:06

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import streams.blocks
import wagtail.blocks
import wagtail.contrib.forms.models
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0083_workflowcontenttype'),
        ('wagtailimages', '0025_alter_image_file_alter_rendition_file'),
        ('webapp', '0016_rename_jobslistingopeninggpage_jobslistingopeningpage'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobsFormDetailOpeningPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('to_address', models.CharField(blank=True, help_text='Optional - form submissions will be emailed to these addresses. Separate multiple addresses by comma.', max_length=255, validators=[wagtail.contrib.forms.models.validate_to_address], verbose_name='to address')),
                ('from_address', models.EmailField(blank=True, max_length=255, verbose_name='from address')),
                ('subject', models.CharField(blank=True, max_length=255, verbose_name='subject')),
                ('category', models.CharField(help_text='Article category', max_length=100, null=True)),
                ('author', models.CharField(help_text='Author Article', max_length=100, null=True)),
                ('bio2', models.CharField(help_text='Author bio', max_length=500, null=True)),
                ('custom_title', models.CharField(help_text='Overwrites article title', max_length=100, null=True)),
                ('custom_subtitle', models.CharField(help_text='Overwrites article subtitle', max_length=100, null=True)),
                ('date', models.DateTimeField(auto_now=True)),
                ('abstract', wagtail.fields.RichTextField(blank=True, verbose_name='Abstract')),
                ('comments', wagtail.fields.RichTextField(blank=True, verbose_name='Mensaje para que nos dejen un comentario')),
                ('thank_you_text', wagtail.fields.RichTextField(blank=True)),
                ('content', wagtail.fields.StreamField([('title_and_text', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(help_text='Agregar un titulo', required=True)), ('text', wagtail.blocks.TextBlock(help_text='Agregar un texto adicional', required=True))])), ('full_richtext', streams.blocks.RichtextBlock()), ('simple_richtext', streams.blocks.SimpleRichtextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('cards', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(help_text='Escribir el titulo', required=True)), ('cards', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('title', wagtail.blocks.CharBlock(max_length=100, required=True)), ('text', wagtail.blocks.TextBlock(max_length=200, required=True)), ('button_page', wagtail.blocks.PageChooserBlock(required=False)), ('button_url', wagtail.blocks.URLBlock(help_text='Si el boto es seleccionado arriba de la pagina', required=False))])))]))], blank=True, null=True, use_json_field=None)),
                ('blog_image', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
            ],
            options={
                'abstract': False,
            },
            bases=(wagtail.contrib.forms.models.FormMixin, 'wagtailcore.page', models.Model),
        ),
        migrations.CreateModel(
            name='JobsFormOpeningPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('clean_name', models.CharField(blank=True, default='', help_text='Safe name of the form field, the label converted to ascii_snake_case', max_length=255, verbose_name='name')),
                ('label', models.CharField(help_text='The label of the form field', max_length=255, verbose_name='label')),
                ('field_type', models.CharField(choices=[('singleline', 'Single line text'), ('multiline', 'Multi-line text'), ('email', 'Email'), ('number', 'Number'), ('url', 'URL'), ('checkbox', 'Checkbox'), ('checkboxes', 'Checkboxes'), ('dropdown', 'Drop down'), ('multiselect', 'Multiple select'), ('radio', 'Radio buttons'), ('date', 'Date'), ('datetime', 'Date/time'), ('hidden', 'Hidden field')], max_length=16, verbose_name='field type')),
                ('required', models.BooleanField(default=True, verbose_name='required')),
                ('choices', models.TextField(blank=True, help_text='Comma or new line separated list of choices. Only applicable in checkboxes, radio and dropdown.', verbose_name='choices')),
                ('default_value', models.TextField(blank=True, help_text='Default value. Comma or new line separated values supported for checkboxes.', verbose_name='default value')),
                ('help_text', models.CharField(blank=True, max_length=255, verbose_name='help text')),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='form_fields', to='webapp.jobsformdetailopeningpage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]
