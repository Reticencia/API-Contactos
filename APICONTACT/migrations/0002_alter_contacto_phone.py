# Generated by Django 5.1.5 on 2025-02-05 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APICONTACT', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacto',
            name='phone',
            field=models.CharField(max_length=15),
        ),
    ]
