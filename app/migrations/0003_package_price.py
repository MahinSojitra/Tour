# Generated by Django 3.2 on 2024-02-08 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20240208_1540'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='price',
            field=models.CharField(default=20000, max_length=50, verbose_name='price'),
            preserve_default=False,
        ),
    ]
