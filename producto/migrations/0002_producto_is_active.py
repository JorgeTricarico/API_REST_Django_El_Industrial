# Generated by Django 5.0.3 on 2024-03-16 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
