# Generated by Django 4.0.3 on 2022-04-07 08:41

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('artifact', '0003_remove_artifact_slug_alter_artifact_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='artifact',
            name='slug',
            field=models.SlugField(default=datetime.datetime(2022, 4, 7, 8, 41, 1, 541142, tzinfo=utc), max_length=30, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='artifact',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]