# Generated by Django 3.2.9 on 2022-04-29 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laptop', '0011_auto_20220428_1741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='number',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]
