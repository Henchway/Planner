# Generated by Django 4.0.5 on 2022-06-11 10:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shift', '0002_rename_end_shift_end_time_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='shift',
            unique_together={('start_time', 'end_time')},
        ),
    ]
