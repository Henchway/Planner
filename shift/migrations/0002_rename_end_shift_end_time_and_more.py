# Generated by Django 4.0.5 on 2022-06-11 08:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shift', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shift',
            old_name='end',
            new_name='end_time',
        ),
        migrations.RenameField(
            model_name='shift',
            old_name='start',
            new_name='start_time',
        ),
    ]
