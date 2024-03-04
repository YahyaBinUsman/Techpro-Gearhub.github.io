# Generated by Django 5.0.1 on 2024-02-05 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gadgets', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='product_images/')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('product_id', models.CharField(max_length=50, unique=True)),
            ],
        ),
    ]
