# Generated by Django 5.0.1 on 2024-02-14 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gadgets', '0018_alter_customuser_options_alter_customuser_managers_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='total_price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
