# Generated by Django 5.0.1 on 2024-02-15 19:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gadgets', '0024_rename_cartitem_id_cartitem_id_remove_cartitem_order_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='cart_item',
        ),
        migrations.AddField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(related_name='orders', through='gadgets.OrderItem', to='gadgets.product'),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='gadgets.product'),
        ),
        migrations.AlterField(
            model_name='order',
            name='total_price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='order',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='gadgets.order'),
        ),
    ]