# Generated by Django 5.0.1 on 2024-02-06 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gadgets', '0010_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='password',
            name='password',
            field=models.CharField(max_length=100),
        ),
    ]
