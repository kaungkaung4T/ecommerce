# Generated by Django 3.2.9 on 2022-04-29 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laptop', '0014_auto_20220428_1809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='number',
            field=models.JSONField(blank=True, default=None, null=True),
        ),
    ]
