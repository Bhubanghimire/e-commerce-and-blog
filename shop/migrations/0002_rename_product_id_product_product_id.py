# Generated by Django 3.2 on 2021-04-24 03:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='product_id',
            new_name='Product_id',
        ),
    ]
