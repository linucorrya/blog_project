# Generated by Django 4.2.4 on 2023-08-15 19:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_interiors2'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='interiors',
            new_name='interior',
        ),
        migrations.DeleteModel(
            name='interiors2',
        ),
    ]