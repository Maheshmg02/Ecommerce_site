# Generated by Django 4.2.3 on 2023-09-04 07:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_alter_product_created_alter_product_updated'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Chategory',
            new_name='Category',
        ),
    ]
