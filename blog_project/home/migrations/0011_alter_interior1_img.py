# Generated by Django 4.2.4 on 2023-08-15 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_interior1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interior1',
            name='img',
            field=models.ImageField(upload_to='pictures'),
        ),
    ]
