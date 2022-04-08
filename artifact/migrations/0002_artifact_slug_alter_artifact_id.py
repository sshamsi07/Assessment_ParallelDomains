# Generated by Django 4.0.3 on 2022-04-07 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artifact', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='artifact',
            name='slug',
            field=models.SlugField(default='', max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='artifact',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
