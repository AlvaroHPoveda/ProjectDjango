# Generated by Django 3.2 on 2022-05-20 20:02

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('location_app', '0016_alter_rack_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rack',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('ee0cc8ab-8030-4d10-84aa-961122960727')),
        ),
    ]
