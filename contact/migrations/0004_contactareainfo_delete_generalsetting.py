# Generated by Django 4.2.2 on 2023-07-22 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_remove_generalsetting_text_parameter_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactAreaInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Updated Date')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('order', models.PositiveIntegerField(default=0, verbose_name='Order')),
                ('title', models.CharField(blank=True, default='', max_length=254, verbose_name='Title')),
                ('description', models.CharField(blank=True, default='', max_length=254, verbose_name='Description')),
                ('icon', models.CharField(blank=True, default='', max_length=254, verbose_name='Icon')),
                ('link', models.CharField(blank=True, default='', verbose_name='Link')),
            ],
            options={
                'verbose_name': 'Contact Area Info',
                'verbose_name_plural': 'Contact Area Infos',
                'ordering': ('order',),
            },
        ),
        migrations.DeleteModel(
            name='GeneralSetting',
        ),
    ]
