# Generated by Django 3.2.9 on 2022-04-29 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laptop', '0012_alter_item_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='number',
        ),
        migrations.AddField(
            model_name='order',
            name='number',
            field=models.ManyToManyField(related_name='item_number', to='laptop.item'),
        ),
    ]
