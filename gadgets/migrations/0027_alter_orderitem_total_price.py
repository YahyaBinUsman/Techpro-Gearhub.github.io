# Generated by Django 5.0.1 on 2024-02-16 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gadgets', '0026_remove_order_products_order_products'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='total_price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=1000),
        ),
    ]