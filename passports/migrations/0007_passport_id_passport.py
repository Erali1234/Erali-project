# Generated by Django 4.1.2 on 2023-07-04 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('passports', '0006_passport_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='passport',
            name='id_passport',
            field=models.CharField(default=1, max_length=9, unique=True),
            preserve_default=False,
        ),
    ]
