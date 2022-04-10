# Generated by Django 4.0.3 on 2022-04-10 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artifact', '0004_artifact_slug_alter_artifact_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artifact',
            name='platform_used',
            field=models.CharField(choices=[('linux', 'Linux'), ('windows', 'Windows')], max_length=10),
        ),
    ]