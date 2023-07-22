# Generated by Django 4.2.2 on 2023-07-22 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_alter_document_file_alter_imagesetting_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='education',
            name='school_location',
            field=models.CharField(blank=True, default='', max_length=254, verbose_name='School Location'),
        ),
        migrations.AddField(
            model_name='generalsetting',
            name='text_parameter',
            field=models.TextField(blank=True, default='', verbose_name='Text Parameter'),
        ),
    ]
