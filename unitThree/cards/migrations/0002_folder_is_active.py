# Generated by Django 5.1.3 on 2024-12-03 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='folder',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]