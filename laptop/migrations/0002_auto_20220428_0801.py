# Generated by Django 3.2.9 on 2022-04-28 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laptop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laptop',
            name='discount',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='image',
            field=models.ImageField(upload_to='media'),
        ),
    ]
