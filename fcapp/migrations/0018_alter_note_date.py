# Generated by Django 4.2.4 on 2023-12-27 00:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fcapp', '0017_alter_note_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 27, 0, 29, 15, 460744, tzinfo=datetime.timezone.utc)),
        ),
    ]
