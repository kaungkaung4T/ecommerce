# Generated by Django 3.2.9 on 2022-04-28 22:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('laptop', '0008_alter_order_items'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='items',
            new_name='newitem',
        ),
    ]