# Generated by Django 4.2.4 on 2023-08-14 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_interiors2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interiors2',
            name='date',
            field=models.DateField(),
        ),
    ]
