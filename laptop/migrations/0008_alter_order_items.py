# Generated by Django 3.2.9 on 2022-04-28 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laptop', '0007_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='items',
            field=models.ManyToManyField(related_name='item_lists', to='laptop.item'),
        ),
    ]
