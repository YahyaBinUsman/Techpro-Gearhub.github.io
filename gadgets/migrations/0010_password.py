# Generated by Django 5.0.1 on 2024-02-06 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gadgets', '0009_alter_product_id_alter_product_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Password',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]