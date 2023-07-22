# Generated by Django 4.2.2 on 2023-07-22 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GeneralSetting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Updated Date')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('name', models.CharField(blank=True, default='', max_length=254, verbose_name='Name')),
                ('description', models.CharField(blank=True, default='', max_length=254, verbose_name='Description')),
                ('parameter', models.CharField(blank=True, default='', max_length=254, verbose_name='Parameter')),
                ('text_parameter', models.TextField(blank=True, default='', verbose_name='Text Parameter')),
            ],
            options={
                'verbose_name': 'General Setting',
                'verbose_name_plural': 'General Settings',
                'ordering': ('name',),
            },
        ),
    ]