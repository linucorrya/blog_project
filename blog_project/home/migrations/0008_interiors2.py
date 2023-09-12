# Generated by Django 4.2.4 on 2023-08-15 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_delete_interiors2'),
    ]

    operations = [
        migrations.CreateModel(
            name='interiors2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('img', models.ImageField(upload_to='picture')),
                ('desc', models.TextField()),
                ('date', models.DateField()),
            ],
        ),
    ]