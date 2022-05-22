# Generated by Django 3.2 on 2022-05-20 01:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('N', 'NARRATIVE'), ('T', 'TERROR'), ('H', 'HUMOR'), ('R', 'ROMANTIC')], max_length=1)),
                ('edition', models.CharField(choices=[('N', 'NARRATIVE'), ('T', 'TERROR'), ('H', 'HUMOR'), ('R', 'ROMANTIC')], max_length=2)),
                ('cover', models.CharField(max_length=25)),
                ('color', models.CharField(max_length=25)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
