# Generated by Django 4.0.5 on 2022-06-11 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('day', '0003_alter_day_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='day',
            name='date',
            field=models.DateField(null=True, unique=True),
        ),
    ]
