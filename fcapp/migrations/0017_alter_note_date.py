# Generated by Django 4.2.4 on 2023-12-20 01:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fcapp', '0016_alter_note_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 20, 1, 33, 19, 601141, tzinfo=datetime.timezone.utc)),
        ),
    ]
