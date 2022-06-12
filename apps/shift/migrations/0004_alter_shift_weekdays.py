# Generated by Django 4.0.5 on 2022-06-12 22:05

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('shift', '0003_alter_shift_unique_together_shift_weekdays_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shift',
            name='weekdays',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday')], max_length=300, null=True),
        ),
    ]
