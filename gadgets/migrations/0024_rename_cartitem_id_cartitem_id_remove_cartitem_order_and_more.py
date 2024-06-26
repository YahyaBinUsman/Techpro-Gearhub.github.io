# Generated by Django 5.0.1 on 2024-02-15 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gadgets', '0023_merge_20240215_2224'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartitem',
            old_name='cartitem_id',
            new_name='id',
        ),
        migrations.RemoveField(
            model_name='cartitem',
            name='order',
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='total_price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterModelTable(
            name='order',
            table=None,
        ),
    ]
