# Generated by Django 3.2.9 on 2022-04-29 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laptop', '0013_auto_20220428_1756'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='number',
        ),
        migrations.AddField(
            model_name='order',
            name='number',
            field=models.JSONField(default=None),
        ),
    ]
