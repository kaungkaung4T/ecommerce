# Generated by Django 3.2.9 on 2022-04-29 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laptop', '0015_alter_order_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='number',
        ),
        migrations.AddField(
            model_name='item',
            name='number',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]
