# Generated by Django 3.1 on 2021-07-05 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_total',
            field=models.FloatField(default=False),
        ),
    ]