# Generated by Django 5.0.1 on 2024-02-15 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gadgets', '0020_alter_order_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
